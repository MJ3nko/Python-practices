import math
from typing import Union


class Complex(object):
    def __init__(self, real: Union[float, int], imaginary: Union[float, int]) -> None:
        self.real: Union[float, int] = real
        self.imaginary: Union[float, int] = imaginary

    def __add__(self, no: "Complex") -> "Complex":
        # Overloaded for + operation
        a: Union[float, int] = self.real
        b: Union[float, int] = self.imaginary
        c: Union[float, int] = no.real
        d: Union[float, int] = no.imaginary
        return Complex(a + c, b + d)

    def __sub__(self, no: "Complex") -> "Complex":
        # Overloaded for - operation
        a: Union[float, int] = self.real
        b: Union[float, int] = self.imaginary
        c: Union[float, int] = no.real
        d: Union[float, int] = no.imaginary
        return Complex(a - c, b - d)

    def __mul__(self, no: "Complex") -> "Complex":
        # Overloaded for * operation
        a: Union[float, int] = self.real
        b: Union[float, int] = self.imaginary
        c: Union[float, int] = no.real
        d: Union[float, int] = no.imaginary
        real_mult: Union[float, int] = (a * c) - (b * d)
        imag_mult: Union[float, int] = (a * d) + (b * c)
        return Complex(real_mult, imag_mult)

    def __truediv__(self, no: "Complex") -> "Complex":
        # Overloaded for / operation
        a: Union[float, int] = self.real
        b: Union[float, int] = self.imaginary
        c: Union[float, int] = no.real
        d: Union[float, int] = no.imaginary
        real_numerator: Union[float, int] = a * c + b * d
        return real_numerator / (c**2 + d**2)

    def __str__(self):
        # Overloaded for str() operation
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

    def mod(self) -> "Complex":
        a: Union[float, int] = self.real
        b: Union[float, int] = self.imaginary
        return Complex(math.sqrt(a**2 + b**2), 0)


if __name__ == "__main__":
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
