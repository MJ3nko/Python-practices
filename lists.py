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
    print(head, body, tail)


def zip_usage():
    names = ['Jenny', 'Alexus', 'Sam', 'Grace']
    dogs_names = ['Elphonse', 'Dr. Doggy DDS', 'Carter', 'Ralph']

    # zip is used to create a tuple
    names_and_dogs_names = zip(names, dogs_names)


if __name__ == "__main__":
    lists_usage()
    unpack_argument_list()
