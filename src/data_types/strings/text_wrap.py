import textwrap


def wrap_string(string, max_width):
    lines = []
    line_count = int(len(string) / max_width) + 1
    for index in range(line_count):
        start = index * max_width
        end = start + max_width
        line = string[start:end]
        lines.append(line)
    lines = join_lines(lines)
    return lines


def textwrap_string(string, max_width):
    string = textwrap.wrap(string, max_width)
    string = join_lines(string)
    return string


def join_lines(lines):
    lines = "\n".join(lines)
    return lines


def main():
    string, max_width = input(), int(input())
    lines = wrap_string(string, max_width)
    print(lines)
    lines = textwrap_string(string, max_width)
    print(lines)


if __name__ == "__main__":
    main()
