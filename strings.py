from string import Template
import sys


def bool_comparison(greetings: bool) -> int:

    # Good
    if greetings:
        return 0

    # Bad, comparison to False should be 'if cond is False:' or 'if not cond:'
    if greetings == False:
        return 1

    # Very bad, redundant code
    if greetings is True:
        return 2


def strings_usage(string_param: str):
    a = 2
    b = 3.14
    name = "Marko" * 1    

    f_strings_output(a, b)
    format_output(a, b)
    raw_string()
    vanilla_output(a, name)


def f_strings_output(a, b):
    print(f"a = {a} and b = {b}")					# Python 3.6+
    print(f"a = {a=}")								# Debug


def format_output(a, b):
    print('a = {x}, b = {y} !'.format(x=a, y=b))    # Python 2.6+
    print('a = ' + str(a) + ', b = ' + str(b))	    # String conversion required


def vanilla_output(a, name):
    print("Hello, %s. A has %s value." % (name, a))
    t = Template('Hey, $name!')
    print(t.substitute(name=name))


def raw_string():
    raw_string = r'Look at all these \n \x \\\ values.'
    print(raw_string)


def check_strings_value(name):
    if name.startswith('Mar') and name.endswith('ko'):
        print("This is a good way to check strings.")
    if name[:3] == 'Mar':
        print("This is a bad way to check strings.")


def main(positional_argument):
    print(f"Sys.argv[1:] values: {positional_argument} \n")


if __name__ == "__main__":
    main(sys.argv[1:])
    strings_usage("Write good code.")
    check_strings_value("Marko")
