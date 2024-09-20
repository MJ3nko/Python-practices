def validators():
    s = input("Enter a string: ")
    print(str(isalnum(s)))
    print(str(isalpha(s)))
    print(str(has_digit(s)))
    print(str(has_lowercase_char(s)))
    print(str(has_uppercase_char(s)))


def isalnum(s):
    return any(char.isalnum() for char in s)


def isalpha(s):
    return any(char.isalpha() for char in s)


def has_uppercase_char(s):
    return any(char.isupper() for char in s)


def has_lowercase_char(s):
    return any(char.islower() for char in s)


def has_digit(s):
    return any(char.isdigit() for char in s)


def main():
    validators()


if __name__ == "__main__":
    main()
