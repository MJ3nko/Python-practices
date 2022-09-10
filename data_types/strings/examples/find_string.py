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


def print_text():
    text = input()
    print(text)
    text = text.swapcase()
    print(text)


def split_and_join(line):
    line = line.split(" ")
    line = "-".join(line)
    return line


def main():
    find_string()


if __name__ == "__main__":
    main()
