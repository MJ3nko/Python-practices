from dataclasses import dataclass, field
from typing import List, Callable, Dict


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
        try:
            self.numbers.remove(number)
        except ValueError:
            print(f"ValueError: {number} not in list")

    def sort(self) -> None:
        self.numbers.sort()

    def reverse(self) -> None:
        self.numbers.reverse()

    def pop(self) -> None:
        if self.numbers:
            self.numbers.pop()
        else:
            print("IndexError: pop from empty list")

    def handle_command(self, command: str, args: List[str]) -> None:
        commands: Dict[str, Callable[[], None]] = {
            "print": self.print,
            "insert": lambda: self.insert(int(args[0]), int(args[1])),
            "append": lambda: self.append(int(args[0])),
            "remove": lambda: self.remove(int(args[0])),
            "sort": self.sort,
            "reverse": self.reverse,
            "pop": self.pop,
        }
        if command in commands:
            try:
                commands[command]()
            except (IndexError, ValueError) as e:
                print(f"Error: {e}")
        else:
            print(f"Unknown command: {command}")


def main() -> None:
    new = Numbers()
    new.handle_command("append", ["10"])
    new.handle_command("insert", ["1", "12"])
    new.handle_command("print")


if __name__ == "__main__":
    main()
