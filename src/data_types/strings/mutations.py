def change_character(string: str, index: int, char: str) -> str:
    return string[:index] + char + string[index + 1:]


def main():
    string = input("Enter the string: ")
    index, char = input("Enter the index and character separated by space: ").split()
    index = int(index)
    
    new_string = change_character(string, index, char)
    print("Modified string:", new_string)


if __name__ == "__main__":
    main()
