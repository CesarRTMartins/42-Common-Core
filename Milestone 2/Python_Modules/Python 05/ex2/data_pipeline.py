import typing
import abc


class DataProcessor(abc.ABC):
    def __init__(self, name: str) -> None:
        self.name = name
        self._total: int = 0
        self._output_index: int = 0
        self._storage: list[typing.Any] = []

    @abc.abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass

    @abc.abstractmethod
    def process(self, data: typing.Any) -> None:
        pass

    def output(self, count: int = 1) -> list[tuple[int, str]]:
        items = self._storage[:count]
        self._storage = self._storage[count:]
        result = []
        for item in items:
            result.append((self._output_index, self._serialize(item)))
            self._output_index += 1
        return result

    @abc.abstractmethod
    def _serialize(self, item: typing.Any) -> str:
        pass

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

    def _serialize(self, item: typing.Any) -> str:
        return str(item)


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

    def _serialize(self, item: typing.Any) -> str:
        return str(item)


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

    def _serialize(self, item: typing.Any) -> str:
        return f"{item['log_level']}: {item['log_message']}"


class ExportPlugin(typing.Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class CSVExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        csv_line = ",".join(value for _, value in data)
        print(f"CSV Output: {csv_line}")


class JSONExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pairs = ", ".join(
            f'"item_{index}": "{value}"'
            for index, value in data
        )
        print(f"JSON Output: {{{pairs}}}")


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
                msg = (f"DataStream error - Can't process"
                       f" element in stream: {element}")
                print(msg)

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self._processors:
            data = proc.output(nb)
            if data:
                plugin.process_output(data)

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data")
            return
        for proc in self._processors:
            print(proc.get_stats())


# === Test scenario ===
print("=== Code Nexus - Data Pipeline ===")
print()
print("Initialize Data Stream...")
print()

ds = DataStream()
ds.print_processors_stats()
print()

print("Registering Processors")
ds.register_processor(NumericProcessor())
ds.register_processor(TextProcessor())
ds.register_processor(LogProcessor())

batch1 = [
    'Hello world',
    [3.14, -1, 2.71],
    [{'log_level': 'WARNING', 'log_message': 'Telnet access! Use ssh instead'},
     {'log_level': 'INFO', 'log_message': 'User wil is connected'}],
    42,
    ['Hi', 'five'],
]
print()

print(f"Send first batch of data on stream: {batch1}")
ds.process_stream(batch1)
print()
ds.print_processors_stats()
print()
csv_plugin = CSVExportPlugin()
print("Send 3 processed data from each processor to a CSV plugin:")
ds.output_pipeline(3, csv_plugin)
print()
ds.print_processors_stats()

batch2 = [
    21,
    ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
    [{'log_level': 'ERROR', 'log_message': '500 server crash'},
     {'log_level': 'NOTICE', 'log_message': 'Certificate expires in 10 days'}],
    [32, 42, 64, 84, 128, 168],
    'World hello',
]

print(f"Send another batch of data: {batch2}")
ds.process_stream(batch2)
print()
ds.print_processors_stats()

json_plugin = JSONExportPlugin()
print("Send 5 processed data from each processor to a JSON plugin:")
ds.output_pipeline(5, json_plugin)
print()
ds.print_processors_stats()
