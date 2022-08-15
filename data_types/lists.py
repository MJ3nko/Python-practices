def lists_usage():
    last_semester_gradebook = [
        ("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]
    subjects = ["physics", "calculus", "poetry", "history"]
    grades = [98, 97, 85, 88]
    full_gradebook = create_and_return_gradebook(
        subjects, grades, last_semester_gradebook)
    reverse_and_print_gradebook(full_gradebook)
    print()


def create_and_return_gradebook(subjects, grades, last_semester_gradebook):
    gradebook = list(zip(subjects, grades))
    full_gradebook = gradebook + last_semester_gradebook
    return full_gradebook


def reverse_and_print_gradebook(full_gradebook):
    full_gradebook.sort(reverse=True)
    print_for_loop_gradebook(full_gradebook)


def print_for_loop_gradebook(gradebook):
    print("Printing gradebook content:")
    for index in range(len(gradebook)):
        print(gradebook[index])


def unpack_argument_list():
    # Python 3.0+
    items = [1, "New", 3.21, 4, 5]
    head, *body, tail = items       # 1 ["New", 3.21, 4] 5


def return_sample_names():
    # create a tuple
    names = ["Jenny", "Alexus", "Sam", "Grace"]
    dog_names = ["Elphonse", "Dr. Doggy DDS", "Carter", "Ralph"]
    return zip(names, dog_names)


def run_method(method):
    usage_text = f"Do you want to execute {method}?\nEnter an option (y or n):"
    while (selected_option := input(usage_text).lower()) not in ["n", "y"]:
        print(f"{selected_option} is not supported. Try again.")
    if selected_option == "y":
        return True
    return False


def list_comprehension_usage_example():
    x = int(input())
    y = int(input())
    z = int(input())
    ignored_sum = int(input())

    combinations = [[a, b, c] for a in range(x+1) for b in range(y+1)
                    for c in range(z+1) if (a + b + c) != ignored_sum]
    print(combinations)


def print_second_largest_number():
    mapper = map(int, input().split())
    numbers = list(mapper)
    first = numbers[0]
    second = numbers[0]

    for number in numbers:
        if number > first:
            second = first
            first = number
        elif first > number > second:
            second = number

    print(f"Second largest number: {second}")


def main():
    if run_method(lists_usage.__name__):
        lists_usage()
    if run_method(unpack_argument_list.__name__):
        unpack_argument_list()
    if run_method(list_comprehension_usage_example.__name__):
        list_comprehension_usage_example()
    if run_method(print_second_largest_number.__name__):
        print_second_largest_number()


if __name__ == "__main__":
    main()
