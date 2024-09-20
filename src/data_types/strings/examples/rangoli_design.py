def print_rangoli(size: int) -> None:
    """
    Prints a Rangoli pattern of the given size.

    Args:
        size (int): The size of the Rangoli.
    """
    highest_char_code = ord('a') + size - 1
    lines = [create_line(i, highest_char_code) for i in range(size)]
    print('\n'.join(lines + lines[-2::-1]))


def create_line(distance: int, highest_char_code: int) -> str:
    """
    Creates a single line of the Rangoli pattern.

    Args:
        distance (int): The distance from the center line.
        highest_char_code (int): The ASCII code of the highest character.

    Returns:
        str: The formatted line of the Rangoli pattern.
    """
    middle_char_code = ord('a') + distance
    alpha_chars = '-'.join(chr(c) for c in range(highest_char_code, middle_char_code, -1))
    line = f"{alpha_chars}-{chr(middle_char_code)}-{alpha_chars[::-1]}"
    return line.center(4 * (highest_char_code - ord('a')) + 1, '-')


if __name__ == "__main__":
    size = int(input("Enter the size of the Rangoli: "))
    print_rangoli(size)