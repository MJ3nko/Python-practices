from dataclasses import dataclass


@dataclass
class Numbers:
    numbers = []

    def print(self):
        print(self.numbers)

    def insert(self, position, number):
        self.numbers.insert(position, number)

    def append(self, number):
        self.numbers.append(number)

    def remove(self, number):
        self.numbers.remove(number)

    def sort(self):
        self.numbers.sort()

    def reverse(self):
        self.numbers.reverse()

    def pop(self):
        self.numbers.pop()

    def list_methods_usage(self):
        number_of_commands = int(input())
        for _ in range(number_of_commands):
            command, *line = input().split()
            self.handle_command(command, line)

    def handle_command(self, command, line=None):
        if command == "print":
            self.print()
        if line:
            if command == "insert":
                position = int(line[0])
                number = int(line[1])
                self.insert(position, number)
            elif command == "append":
                number = int(line)
                self.append(number)
            elif command == "remove":
                number = int(line)
                self.remove(number)
            elif command == "sort":
                self.sort()
            elif command == "reverse":
                self.reverse()
            elif command == "pop":
                self.pop()


def main():
    new = Numbers()
    new.handle_command("append", 10)
    new.handle_command("insert", [1, 12])
    new.handle_command("print")


if __name__ == '__main__':
    main()
