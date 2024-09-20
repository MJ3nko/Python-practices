import math
from typing import Union


class Complex:
    def __init__(self, real: Union[float, int], imaginary: Union[float, int]) -> None:
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other: "Complex") -> "Complex":
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def __sub__(self, other: "Complex") -> "Complex":
        return Complex(self.real - other.real, self.imaginary - other.imaginary)

    def __mul__(self, other: "Complex") -> "Complex":
        real = self.real * other.real - self.imaginary * other.imaginary
        imag = self.real * other.imaginary + self.imaginary * other.real
        return Complex(real, imag)

    def __truediv__(self, other: "Complex") -> "Complex":
        denominator = other.real**2 + other.imaginary**2
        real = (self.real * other.real + self.imaginary * other.imaginary) / denominator
        imag = (self.imaginary * other.real - self.real * other.imaginary) / denominator
        return Complex(real, imag)

    def __str__(self) -> str:
        real_str = f"{self.real:.2f}"
        imag_str = f"{abs(self.imaginary):.2f}i"
        sign = '+' if self.imaginary >= 0 else '-'
        if self.imaginary == 0:
            return f"{real_str}+0.00i"
        if self.real == 0:
            return f"0.00{sign}{imag_str}"
        return f"{real_str}{sign}{imag_str}"

    def mod(self) -> "Complex":
        modulus = math.sqrt(self.real**2 + self.imaginary**2)
        return Complex(modulus, 0)


def main():
    c = list(map(float, input().split()))
    d = list(map(float, input().split()))
    x = Complex(c[0], c[1])
    y = Complex(d[0], d[1])
    print(x + y)
    print(x - y)
    print(x * y)
    print(x / y)
    print(x.mod())
    print(y.mod())


if __name__ == "__main__":
    main()
