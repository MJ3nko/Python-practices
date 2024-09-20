def print_second_lowest_grade_names(students):
    second_lowest_grade = get_second_lowest_grade(students)
    names = get_students_with_grade(students, second_lowest_grade)
    for name in sorted(names):
        print(name)


def get_second_lowest_grade(students):
    grades = sorted(set(score for _, score in students))
    return grades[1] if len(grades) > 1 else None


def get_students_with_grade(students, grade):
    return [name for name, score in students if score == grade]


def main():
    students = []
    for _ in range(int(input("Enter number of students: "))):
        name = input("Enter student name: ")
        score = float(input("Enter student score: "))
        students.append([name, score])
    print_second_lowest_grade_names(students)


if __name__ == "__main__":
    main()
