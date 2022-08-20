import sys
from string import Template


class Guideline:
    def __init__(self) -> None:
        pass

    def bool_comparison_example(self):
        guideline = """
        value = 0
        # Good
        if value:
            return 0

        # Bad, should be 'if cond is False:' or 'if not cond:'
        if value == False:
            return 1

        # Very bad, redundant code
        if value is True:
            return 2
        """
        print(guideline)

    def quotation_marks(self):
        guideline = """
        You can use various types of quotation marks inside the expressions.
        Just make sure you are not using the same type of quotation mark
        on the outside of the f-string as you are using in the expression.
        """
        print(guideline)

    def string_quotes(self):
        guideline = """
        Single-quoted strings and double-quoted strings are the same.
        Choose one and stick to it.

        When a string contains single or double quote characters,
        use the other one to avoid backslashes in the string.
        It improves readability.

        For triple-quoted strings, always use double quote characters
        to be consistent with the docstring convention in PEP 257.
        """
        print(guideline)

    def check_strings_implementation(self, name):
        prefix = "Mar"
        suffix = "ko"
        if name.startswith(prefix) and name.endswith(suffix):
            print("This is a good way to check strings.")
        if name[:3] == prefix:
            print("This is a bad way to check strings.")


def strings_usage(string_param: str):
    favorite_number = 7
    pi = 3.14159265359
    name = "Marko" * 1

    f_strings_output(favorite_number, pi)
    format_output(favorite_number, pi)
    raw_string()
    template_strings_output(name)
    legacy_output(favorite_number, name)


def f_strings_output(favorite_number: int, pi: float):
    # Python 3.6+
    print(f"favorite number = {favorite_number} and pi = {pi}")
    print(f"favorite number debug = {favorite_number=}")


def format_output(favorite_number: int, pi: float):
    # Python 2.6+
    print("favorite number = {x}, pi = {y} !".format(
        x=favorite_number, y=pi))
    print("favorite number = " + str(favorite_number) +
          ", pi = " + str(pi))


def template_strings_output(name: str):
    template = Template("Hey, $name!")
    print(template.substitute(name=name))


def legacy_output(favorite_number: int, name: str):
    print("Hello, %s. favorite number has %s value." % (name, favorite_number))


def raw_string():
    raw_string = r"Look at all these \n \x \\\ values."
    print(raw_string)


def print_text():
    text = input()
    print(text)
    text = text.swapcase()
    print(text)


def split_and_join(line):
    line = line.split(" ")
    line = "-".join(line)
    return line


def find_string():
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)


def count_substring(string, sub_string):
    counter = 0
    for index in range(0, len(string)):
        look_string = string[index:index+len(sub_string)]
        if look_string == sub_string:
            counter += 1
    return counter


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
    positional_arguments = sys.argv[:]
    print(f"Sys.argv[:] values: {positional_arguments} \n")
    strings_usage("Write good code.")
    find_string()


if __name__ == "__main__":
    main()
