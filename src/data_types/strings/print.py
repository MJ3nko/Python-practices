import sys
from string import Template


class Guideline:
    def bool_comparison_example(self) -> None:
        """Demonstrates good and bad practices for boolean comparisons."""
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

    def quotation_marks(self) -> None:
        """Guidelines for using quotation marks in strings."""
        guideline = """
        You can use various types of quotation marks inside the expressions.
        Just make sure you are not using the same type of quotation mark
        on the outside of the f-string as you are using in the expression.
        """
        print(guideline)

    def string_quotes(self) -> None:
        """Guidelines for using single, double, and triple quotes in strings."""
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

    def check_strings_implementation(self, name: str) -> None:
        """Demonstrates good and bad practices for checking string prefixes
        and suffixes."""
        prefix = "Mar"
        suffix = "ko"
        if name.startswith(prefix) and name.endswith(suffix):
            print("This is a good way to check strings.")
        if name[:3] == prefix:
            print("This is a bad way to check strings.")


def strings_usage(string_param: str) -> None:
    """Demonstrates various string formatting techniques."""
    favorite_number = 7
    pi = 3.14159265359
    name = "Marko"

    f_strings_output(favorite_number, pi)
    format_output(favorite_number, pi)
    raw_string_example()
    template_strings_output(name)
    legacy_output(favorite_number, name)


def f_strings_output(favorite_number: int, pi: float) -> None:
    """Demonstrates f-string usage."""
    print(f"favorite number = {favorite_number} and pi = {pi}")
    print(f"favorite number debug = {favorite_number=}")


def format_output(favorite_number: int, pi: float) -> None:
    """Demonstrates str.format() usage."""
    print("favorite number = {x}, pi = {y} !".format(x=favorite_number, y=pi))
    print(f"favorite number = {favorite_number}, pi = {pi}")


def raw_string_example() -> None:
    """Demonstrates raw string usage."""
    raw_string = r"Look at all these \n \x \\\ values."
    print(raw_string)


def template_strings_output(name: str) -> None:
    """Demonstrates Template strings usage."""
    template = Template("Hey, $name!")
    print(template.substitute(name=name))


def legacy_output(favorite_number: int, name: str) -> None:
    """Demonstrates legacy string formatting."""
    print("Hello, %s. favorite number has %s value." % (name, favorite_number))


def main() -> None:
    """Main function to execute the script."""
    positional_arguments = sys.argv[:]
    print(f"Sys.argv[:] values: {positional_arguments} \n")
    strings_usage("Write good code.")


if __name__ == "__main__":
    main()
