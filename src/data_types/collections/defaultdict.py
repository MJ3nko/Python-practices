from collections import defaultdict


def get_input_elements(elements_count: int):
    elements = []
    for _ in range(elements_count):
        elements.append(input())
    return elements


def check_word_occurrence(group_container, group_a, group_b):
    for b_element in group_container[group_b]:
        index_values = [
            str(index + 1)
            for index, a_element in enumerate(group_container[group_a])
            if a_element == b_element
        ]
        print(" ".join(index_values) if index_values else "-1")


def main():
    first_line = list(map(int, input().split()))
    group_container = defaultdict(list)
    group_container["group_a"] = get_input_elements(first_line[0])
    group_container["group_b"] = get_input_elements(first_line[1])
    check_word_occurrence(group_container, "group_a", "group_b")


if __name__ == "__main__":
    main()
