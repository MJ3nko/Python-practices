def print_formatted(number):
    width = len(bin(number)) - 2
    for value in range(1, number + 1):
        decimal = str(value).rjust(width)
        octal = oct(value)[2:].rjust(width)
        hexadecimal = hex(value)[2:].upper().rjust(width)
        binary = bin(value)[2:].rjust(width)
        print(f"{decimal} {octal} {hexadecimal} {binary}")


if __name__ == "__main__":
    number = int(input("Enter a number: "))
    print_formatted(number)
