from __future__ import annotations
from abc import ABC, abstractmethod
from collections.abc import Sequence
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._data: list[str] = []
        self._rank: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Check if data is valid for this processor."""
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        """Process and store valid data. Raise exception if invalid."""
        pass

    def output(self) -> tuple[int, str]:
        """Return (rank, data) tuple and remove it from internal storage."""
        if not self._data:
            raise Exception("No data to output")
        item = self._data.pop(0)
        rank = self._rank
        self._rank += 1
        return (rank, item)


# === Specialized Processors ===

class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if (
            isinstance(data, Sequence)
            and not isinstance(data, str)
            and all(isinstance(x, (int, float)) for x in data)
        ):
            return True
        return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise Exception("Improper numeric data")
        if isinstance(data, Sequence) and not isinstance(data, str):
            self._data.extend(str(x) for x in data)
        else:
            self._data.append(str(data))


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if (
            isinstance(data, Sequence)
            and not isinstance(data, str)
            and all(isinstance(x, str) for x in data)
        ):
            return True
        return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise Exception("Improper text data")
        if isinstance(data, Sequence) and not isinstance(data, str):
            self._data.extend(data)
        else:
            self._data.append(data)


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if (
            isinstance(data, dict)
            and all(isinstance(k, str) and isinstance(v, str)
                    for k, v in data.items())
        ):
            return True
        if (
            isinstance(data, Sequence)
            and not isinstance(data, str)
            and all(
                isinstance(d, dict)
                and all(isinstance(k, str) and isinstance(v, str)
                        for k, v in d.items())
                for d in data
            )
        ):
            return True
        return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise Exception("Improper log data")
        if isinstance(data, Sequence) and not isinstance(data, str):
            for entry in data:
                msg = f"{entry['log_level']}: {entry['log_message']}"
                self._data.append(msg)
        else:
            msg = f"{data['log_level']}: {data['log_message']}"
            self._data.append(msg)


# === Simple Test Harness ===
if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===")
    print()

    # Numeric Processor
    print("Testing Numeric Processor...")
    np = NumericProcessor()
    print(f"Trying to validate input '42': {np.validate(42)}")
    print(f"Trying to validate input 'Hello': {np.validate('Hello')}")
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        np.ingest("foo")  # intentionally invalid
    except Exception as e:
        print(f"Got exception: {e}")
    data = [1, 2, 3, 4, 5]
    print(f"Processing data: {data}")
    np.ingest(data)
    print("Extracting 3 values...")
    for _ in range(3):
        rank, value = np.output()
        print(f"Numeric value {rank}: {value}")
    print()

    # Text Processor
    print("Testing Text Processor...")
    tp = TextProcessor()
    print(f"Trying to validate input '42': {tp.validate('42')}")
    text_data = ["Hello", "Nexus", "World"]
    print(f"Processing data: {text_data}")
    tp.ingest(text_data)
    print("Extracting 1 value...")
    rank, value = tp.output()
    print(f"Text value {rank}: {value}")
    print()

    # Log Processor
    print("Testing Log Processor...")
    lp = LogProcessor()
    print(f"Trying to validate input 'Hello': {lp.validate('Hello')}")
    logs = [
        {"log_level": "NOTICE", "log_message": "Connection to server"},
        {"log_level": "ERROR", "log_message": "Unauthorized access!!"},
    ]
    print(f"Processing data: {logs}")
    lp.ingest(logs)
    print("Extracting 2 values...")
    for i in range(2):
        rank, value = lp.output()
        print(f"Log entry {i}: {value}")
