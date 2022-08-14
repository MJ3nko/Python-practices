def lists_usage():
    last_semester_gradebook = [
        ("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]
    subjects = ["physics", "calculus", "poetry", "history"]
    grades = [98, 97, 85, 88]
    full_gradebook = merge_tuples(subjects, grades, last_semester_gradebook)
    reverse_and_print_gradebook(full_gradebook)


def merge_tuples(subjects, grades, last_semester_gradebook):
    # create a list of tuples
    gradebook = list(zip(subjects, grades))
    full_gradebook = gradebook + last_semester_gradebook
    print(full_gradebook)
    return full_gradebook


def reverse_and_print_gradebook(full_gradebook):
    full_gradebook.sort(reverse=True)
    for_loop(full_gradebook)


def for_loop(gradebook):
    print("Printing gradebook:")
    for index in range(len(gradebook)):
        print(gradebook[index])
    print()


def unpack_argument_list():
    items = [1, "New", 3.21, 4, 5]
    head, *body, tail = items		# Python 3.0+
    print(head, body, tail)         # 1 ["New", 3.21, 4] 5


def zip_usage():
    names = ["Jenny", "Alexus", "Sam", "Grace"]
    dogs_names = ["Elphonse", "Dr. Doggy DDS", "Carter", "Ralph"]

    # zip is used to create a tuple
    names_and_dogs_names = zip(names, dogs_names)


def list_comprehension_usage():

    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    newlist = [[a, b, c] for a in range(x+1) for b in range(y+1)
               for c in range(z+1) if (a + b + c) != n]
    print(newlist)


def print_second_largest_number():
    n = int(input())
    arr = map(int, input().split())
    arr_list = list(arr)
    first = arr_list[0]
    second = arr_list[0]

    for number in arr_list:
        if number > first:
            second = first
            first = number
        elif first > number > second:
            second = number

    print(second)


if __name__ == "__main__":
    lists_usage()
    unpack_argument_list()
    list_comprehension_usage()
    print_second_largest_number()
