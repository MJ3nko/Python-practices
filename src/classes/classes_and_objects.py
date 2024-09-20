from dataclasses import dataclass
from enum import Enum


class Rectangle:
    def __init__(self, color: str, width: float, height: float) -> None:
        self.color = color
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def __repr__(self) -> str:
        return f"Rectangle(color={self.color}, width={self.width}, height={self.height})"


@dataclass
class Square:
    color: str
    width: float
    height: float

    def area(self) -> float:
        return self.width * self.height


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

    @staticmethod
    def print_colors():
        print(repr(Color.RED))
        print(Color.GREEN)
        print(type(Color.BLUE))


def object_type_comparison(obj: object):
    if isinstance(obj, int):
        print("Good practice with isinstance.")
    if type(obj) is int:
        print("Bad practice with type.")


def compare_class_objects():
    rectangle_one = Rectangle("Blue", 2, 3)
    rectangle_two = Square("Blue", 2, 3)

    print(rectangle_one)
    print(rectangle_two)
    print(rectangle_one == rectangle_two)


def main():
    number = 10
    object_type_comparison(number)
    compare_class_objects()


if __name__ == "__main__":
    main()
