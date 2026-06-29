import typing
import abc


class DataProcessor(abc.ABC):
    def __init__(self, name: str) -> None:
        self.name = name
        self._total: int = 0
        self._storage: list[typing.Any] = []

    @abc.abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass

    @abc.abstractmethod
    def process(self, data: typing.Any) -> None:
        pass

    def output(self, count: int = 1) -> list[typing.Any]:
        result = self._storage[:count]
        self._storage = self._storage[count:]
        return result

    def get_stats(self) -> str:
        return (f"{self.name}: total {self._total} items processed, "
                f"remaining {len(self._storage)} on processor")


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__("Numeric Processor")

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, (int, float)) and not isinstance(data, bool):
            return True
        if (
            isinstance(data, list)
            and all(isinstance(x, (int, float)) and not isinstance(x, bool)
                    for x in data)
        ):
            return True
        return False

    def process(self, data: typing.Any) -> None:
        if isinstance(data, list):
            self._total += len(data)
            self._storage.extend(data)
        else:
            self._total += 1
            self._storage.append(data)


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__("Text Processor")

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, str):
            return True
        if (
            isinstance(data, list)
            and all(isinstance(x, str) for x in data)
        ):
            return True
        return False

    def process(self, data: typing.Any) -> None:
        if isinstance(data, list):
            self._total += len(data)
            self._storage.extend(data)
        else:
            self._total += 1
            self._storage.append(data)


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__("Log Processor")

    def validate(self, data: typing.Any) -> bool:
        if (
            isinstance(data, dict)
            and all(isinstance(k, str) and isinstance(v, str)
                    for k, v in data.items())
        ):
            return True
        if (
            isinstance(data, list)
            and all(
                isinstance(d, dict)
                and all(isinstance(k, str) and isinstance(v, str)
                        for k, v in d.items())
                for d in data
            )
        ):
            return True
        return False

    def process(self, data: typing.Any) -> None:
        if isinstance(data, list):
            self._total += len(data)
            self._storage.extend(data)
        else:
            self._total += 1
            self._storage.append(data)


class DataStream:
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        for element in stream:
            handled = False
            for proc in self._processors:
                if proc.validate(element):
                    proc.process(element)
                    handled = True
                    break
            if not handled:
                print(f"DataStream error - Can't process element"
                      f" in stream: {element}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data")
            return
        for proc in self._processors:
            print(proc.get_stats())


# === Test scenario ===
print("=== Code Nexus - Data Stream ===")
print()
print("Initialize Data Stream...")

ds = DataStream()
ds.print_processors_stats()
print()

print("Registering Numeric Processor")
ds.register_processor(NumericProcessor())

batch = [
    'Hello world',
    [3.14, -1, 2.71],
    [{'log_level': 'WARNING', 'log_message': 'Telnet access! Use ssh instead'},
        {'log_level': 'INFO', 'log_message': 'User wil is connected'}],
    42,
    ['Hi', 'five'],
]

print(f"Send first batch of data on stream: {batch}")
ds.process_stream(batch)
ds.print_processors_stats()
print()

print("Registering other data processors")
ds.register_processor(TextProcessor())
ds.register_processor(LogProcessor())

print("Send the same batch again")
ds.process_stream(batch)
ds.print_processors_stats()
print()

print("Consume some elements from the data processors: "
      "Numeric 3, Text 2, Log 1")

numeric_proc = ds._processors[0]
numeric_proc.output(3)

text_proc = ds._processors[1]
text_proc.output(2)

log_proc = ds._processors[2]
log_proc.output(1)

ds.print_processors_stats()
