def print_formatted(number):
    width = len(str(bin(number).split(sep="b")[1]))
    for value in range(1, number + 1):
        decimal = str(value)
        octal = str(oct(value).split(sep="o")[1])
        hexadecimal = str(hex(value).split(sep="x")[1]).upper()
        binary = str(bin(value).split(sep="b")[1])

        decimal = add_spaces(decimal, width)
        octal = add_spaces(octal, width)
        hexadecimal = add_spaces(hexadecimal, width)
        binary = add_spaces(binary, width)
        print(f"{decimal} {octal} {hexadecimal} {binary}")


def add_spaces(value, width):
    value = " " * (width - len(value)) + value
    return value


if __name__ == "__main__":
    number = int(input())
    print_formatted(number)
