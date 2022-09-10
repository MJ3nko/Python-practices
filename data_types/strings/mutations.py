def change_character(string: str, index: int, char: str) -> str:
    string = list(string)
    string[index] = char
    string = "".join(string)
    return string


def slice_string_and_join_character(string: str, index: int, char: str) -> str:
    string = string[:index] + char + string[index+1:]
    return string


def main():
    string = input()
    index, char = input().split()
    new_string = change_character(string, int(index), char)
    new_string = slice_string_and_join_character(string, int(index), char)
    print(new_string)


if __name__ == '__main__':
    main()
