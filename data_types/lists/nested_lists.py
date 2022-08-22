def get_second_lowest_grade(students):
    lowest_grade = students[0][1]
    second_lowest_grade = students[0][1]
    for _, grade in students:
        if grade == lowest_grade:
            pass
        elif grade < lowest_grade:
            second_lowest_grade = lowest_grade
            lowest_grade = grade
        elif grade < second_lowest_grade:
            second_lowest_grade = grade
        elif lowest_grade == second_lowest_grade:
            second_lowest_grade = grade
    return second_lowest_grade


def get_second_lowest_grade_names(students, grade):
    names = []
    for name, score in students:
        if grade == score:
            names.append(name)
    names.sort()
    return names


def print_second_lowest_grade_names(students):
    grade = get_second_lowest_grade(students)
    names = get_second_lowest_grade_names(students, grade)
    for name in names:
        print(name)


if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    print_second_lowest_grade_names(students)
