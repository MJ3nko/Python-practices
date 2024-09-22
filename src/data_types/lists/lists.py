def lists_usage():
    last_semester_gradebook = [
        ("politics", 80),
        ("latin", 96),
        ("dance", 97),
        ("architecture", 65),
    ]
    subjects = ["physics", "calculus", "poetry", "history"]
    grades = [98, 97, 85, 88]
    full_gradebook = create_and_return_gradebook(
        subjects, grades, last_semester_gradebook
    )
    reverse_and_print_gradebook(full_gradebook)
    print()


def reverse_and_print_gradebook(full_gradebook):
    full_gradebook.sort(reverse=True)
    print_for_loop_gradebook(full_gradebook)


def create_and_return_gradebook(subjects, grades, last_semester_gradebook):
    gradebook = list(zip(subjects, grades))
    full_gradebook = gradebook + last_semester_gradebook
    return full_gradebook


def print_for_loop_gradebook(gradebook):
    print("Printing gradebook content:")
    for subject, grade in gradebook:
        print(f"{subject}: {grade}")


def unpack_argument_list():
    items = [1, "New", 3.21, 4, 5]
    head, *body, tail = items
    print(f"Head: {head}, Body: {body}, Tail: {tail}")


def return_sample_names():
    names = ["Jenny", "Alexus", "Sam", "Grace"]
    dog_names = ["Elphonse", "Dr. Doggy DDS", "Carter", "Ralph"]
    return list(zip(names, dog_names))


def run_method(method):
    usage_help = f"Do you want to execute {method}?\nEnter an option (y or n):"
    while (selected_option := input(usage_help).lower()) not in ["y", "n"]:
        print(f"{selected_option} is not supported. Try again.")
    return selected_option == "y"


def list_comprehension_usage_example():
    first = int(input("Enter first number: "))
    second = int(input("Enter second number: "))
    third = int(input("Enter third number: "))
    ignored_sum = int(input("Enter the sum to ignore: "))

    combinations = [
        [a, b, c]
        for a in range(first + 1)
        for b in range(second + 1)
        for c in range(third + 1)
        if (a + b + c) != ignored_sum
    ]
    print(combinations)


def print_second_largest_number():
    numbers = list(map(int, input("Enter numbers separated by space: ").split()))
    first, second = float("-inf"), float("-inf")

    for number in numbers:
        if number > first:
            second = first
            first = number
        elif first > number > second:
            second = number

    print(f"Second largest number: {second}")


def print_the_average_percentage():
    number_of_lines = int(input("Enter number of students: "))
    student_score = {}
    for _ in range(number_of_lines):
        name, *line = input("Enter student name and scores: ").split()
        scores = list(map(float, line))
        student_score[name] = scores
    query_name = input("Enter student name to query: ")
    average = return_average_student_score(student_score[query_name])
    print(f"{average:.2f}")


def return_average_student_score(student_scores):
    total = sum(student_scores)
    average = total / len(student_scores)
    return average


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
