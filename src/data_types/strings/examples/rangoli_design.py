def print_rangoli(size):
    highest_char = ord('a') + size - 1
    lines = [create_line(i, highest_char) for i in range(size)]
    print('\n'.join(lines + lines[-2::-1]))


def create_line(distance, highest_char):
    middle_char = ord('a') + distance
    alpha_chars = '-'.join(chr(c) for c in range(highest_char, middle_char, -1))
    line = f"{alpha_chars}-{chr(middle_char)}-{alpha_chars[::-1]}"
    return line.center(4 * (highest_char - ord('a')) + 1, '-')


if __name__ == "__main__":
    number = int(input("Enter the size of the Rangoli: "))
    print_rangoli(number)
