from collections import defaultdict


def add_elements(elements_count: int):
    elements = list()
    for _ in range(elements_count):
        char = input()
        elements.append(char)
    return elements


def check_word_occurrence(group_container, group_a, group_b):
    for b_element in group_container[group_b]:
        index_values = list()
        for index, a_element in enumerate(group_container[group_a]):
            if a_element == b_element:
                index_values.append(str(index + 1))
        print_indexes(index_values)


def print_indexes(index_values):
    if len(index_values) > 0:
        line = " ".join(index_values)
        print(line)
    else:
        print("-1")


def main():
    first_line = list(map(int, input().split(" ")))
    group_container = defaultdict()
    group_container["group_a"] = add_elements(first_line[0])
    group_container["group_b"] = add_elements(first_line[1])
    check_word_occurrence(group_container, "group_a", "group_b")


if __name__ == "__main__":
    main()
