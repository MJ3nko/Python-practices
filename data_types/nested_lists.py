def get_second_lowest_grade(students):
    lowest_grade = students[0][1]
    second_lowest_grade = students[0][1]
    for _, score in students:
        if score == lowest_grade:
            pass
        elif score < lowest_grade:
            second_lowest_grade = lowest_grade
            lowest_grade = score
        elif score < second_lowest_grade:
            second_lowest_grade = score
        elif lowest_grade == second_lowest_grade:
            second_lowest_grade = score
    return second_lowest_grade


def get_second_lowest_grade_names(students, grade):
    names = []
    for name, score in students:
        if grade == score:
            names.append(name)
    names.sort()
    return names


def print_second_lowest_grade(students):
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
    print_second_lowest_grade(students)
