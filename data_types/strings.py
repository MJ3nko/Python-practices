import sys
from string import Template


def bool_comparison(value: bool) -> int:
    # Good
    if value:
        return 0

    # Bad, comparison to False should be 'if cond is False:' or 'if not cond:'
    if value == False:
        return 1

    # Very bad, redundant code
    if value is True:
        return 2


def strings_usage(string_param: str):
    a = 2
    b = 3.14
    name = "Marko" * 1

    f_strings_output(a, b)
    format_output(a, b)
    raw_string()
    template_strings_output(name)
    vanilla_output(a, name)


def f_strings_output(a, b):
    print(f"a = {a} and b = {b}")					# Python 3.6+
    print(f"debug = {a=}")							# Debug


def format_output(a, b):
    print("a = {x}, b = {y} !".format(x=a, y=b))    # Python 2.6+
    print("a = " + str(a) + ", b = " + str(b))	    # String conversion required


def template_strings_output(name):
    t = Template("Hey, $name!")
    print(t.substitute(name=name))


def vanilla_output(value, name):
    print("Hello, %s. A has %s value." % (name, value))


def raw_string():
    raw_string = r"Look at all these \n \x \\\ values."
    print(raw_string)


def check_strings_value(name):
    first_part = "Mar"
    second_part = "ko"
    if name.startswith(first_part) and name.endswith(second_part):
        print("This is a good way to check strings.")
    if name[:3] == first_part:
        print("This is a bad way to check strings.")


def quotation_marks():
    guideline = """
    You can use various types of quotation marks inside the expressions.
    Just make sure you are not using the same type of quotation mark
    on the outside of the f-string as you are using in the expression.
    """
    print(guideline)


def string_quotes():
    guideline = """
    In Python, single-quoted strings and double-quoted strings are the same.
    Choose one and stick to it.

    When a string contains single or double quote characters,
    use the other one to avoid backslashes in the string.
    It improves readability.

    For triple-quoted strings, always use double quote characters
    to be consistent with the docstring convention in PEP 257.
    """
    print(guideline)


def swap_case():
    s = input()
    result = s.swapcase()
    print(result)

    return


def main(positional_arguments):
    print(f"Sys.argv[:] values: {positional_arguments} \n")
    strings_usage("Write good code.")
    check_strings_value("Marko")


if __name__ == "__main__":
    main(sys.argv[:])
