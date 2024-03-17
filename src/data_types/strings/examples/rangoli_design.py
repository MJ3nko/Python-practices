def print_rangoli(size):
    highest_char = ord("a") + size - 1
    print_top_half(size, highest_char)
    print_bottom_half(size, highest_char)


def print_top_half(size, highest_char):
    for distance in range(size - 1, -1, -1):
        write_line(distance, highest_char)


def print_bottom_half(size, highest_char):
    for distance in range(1, size):
        write_line(distance, highest_char)


def write_line(distance, highest_char):
    minus_chars = "-" * (2 * (distance))
    middle_char = ord("a") + distance
    alpha_chars = return_alpha_chars(highest_char, middle_char)
    left_side = f"{minus_chars}{alpha_chars}"
    right_side = left_side[::-1]
    print(f"{left_side}{chr(middle_char)}{right_side}")


def return_alpha_chars(starting_char, end_char):
    if end_char == starting_char:
        return ""
    line = ""
    for char in range(starting_char, end_char, -1):
        line += f"{chr(char)}-"
    return line


if __name__ == "__main__":
    number = int(input())
    print_rangoli(number)
