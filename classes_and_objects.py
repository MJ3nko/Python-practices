from dataclasses import dataclass
from enum import Enum


class Rectangle1:
    def __init__(
            self,
            color: str,
            width: float,
            height: float) -> None:

        self.color = color
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

#  Using data classes, Python will automatically
#  generate special methods like "_init__" and "__repr__",
#  reducing a lot of the clutter from your code.


@dataclass
class Rectangle2:
    color: str
    width: float
    height: float

    def area(self) -> float:
        return self.width * self.height

# Instead of cluttering your code with constants, you can create an enumeration using the Enum class.
# An Enumeration is a set of symbolic names bound to unique, constant values.


class Color(Enum):
    RED = 1,
    GREEN = 2,
    BLUE = 3,

    def print_colors():
        print(repr(Color.RED))      # <Color.RED: (1,)>
        print(Color.GREEN)          # Color.GREEN
        print(type(Color.BLUE))     # <enum 'Color'>


def object_type_comparison(obj: object):
    if isinstance(obj, int):
        print("Good practice with isinstance.")
    if type(obj) is type(int):
        print("Bad practice with type.")


def compare_class_objects():
    rectangle1 = Rectangle1("Blue", 2, 3)
    rectangle2 = Rectangle2("Blue", 2, 3)

    # <__main__.Rectangle1 object at 0x00000212DC9C60E0>
    # Rectangle2(color='Blue', width=2, height=3)
    # False
    print(rectangle1)
    print(rectangle2)
    print(rectangle1 == rectangle2)
    del rectangle1, rectangle2
    print("Deleted all objects.")


if __name__ == "__main__":
    number = 10
    object_type_comparison(number)
    compare_class_objects()
