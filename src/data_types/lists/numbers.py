from dataclasses import dataclass, field
from typing import List


@dataclass
class Numbers:
    numbers: List[int] = field(default_factory=list)

    def print(self) -> None:
        print(self.numbers)

    def insert(self, position: int, number: int) -> None:
        self.numbers.insert(position, number)

    def append(self, number: int) -> None:
        self.numbers.append(number)

    def remove(self, number: int) -> None:
        self.numbers.remove(number)

    def sort(self) -> None:
        self.numbers.sort()

    def reverse(self) -> None:
        self.numbers.reverse()

    def pop(self) -> None:
        self.numbers.pop()

    def list_methods_usage(self) -> None:
        number_of_commands = int(input())
        for _ in range(number_of_commands):
            command, *line = input().split()
            self.handle_command(command, line)

    def handle_command(self, command: str, line: List[str]) -> None:
        commands = {
            "print": self.print,
            "insert": lambda: self.insert(int(line[0]), int(line[1])),
            "append": lambda: self.append(int(line[0])),
            "remove": lambda: self.remove(int(line[0])),
            "sort": self.sort,
            "reverse": self.reverse,
            "pop": self.pop,
        }
        if command in commands:
            commands[command]()


def main() -> None:
    new = Numbers()
    new.handle_command("append", ["10"])
    new.handle_command("insert", ["1", "12"])
    new.handle_command("print")


if __name__ == "__main__":
    main()
