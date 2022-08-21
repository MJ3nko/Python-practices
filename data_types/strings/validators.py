def has_uppercase_char(s):
    for char in s:
        if char >= "A" and char <= "Z":
            return True
    return False


def has_lowercase_char(s):
    for char in s:
        if char >= "a" and char <= "z":
            return True
    return False


def has_digit(s):
    for char in s:
        if char >= "0" and char <= "9":
            return True
    return False


def isalnumeric(s):
    if has_lowercase_char(s) or has_uppercase_char(s) or has_digit(s):
        return True
    return False


def isalpha(s):
    if has_lowercase_char(s) or has_uppercase_char(s):
        return True
    return False


def validators():
    s = input()
    if isalnumeric(s):
        print("True")
    else:
        print("False")
    if isalpha(s):
        print("True")
    else:
        print("False")
    if has_digit(s):
        print("True")
    else:
        print("False")
    if has_lowercase_char(s):
        print("True")
    else:
        print("False")
    if has_uppercase_char(s):
        print("True")
    else:
        print("False")


def main():
    validators()


if __name__ == "__main__":
    main()
