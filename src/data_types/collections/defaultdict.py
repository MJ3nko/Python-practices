from collections import defaultdict


def add_elements(elements_count: int):
    return [input() for _ in range(elements_count)]


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
    group_container["group_a"] = add_elements(first_line[0])
    group_container["group_b"] = add_elements(first_line[1])
    check_word_occurrence(group_container, "group_a", "group_b")


if __name__ == "__main__":
    main()
