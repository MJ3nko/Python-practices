from typing import List, Tuple, Optional

def print_second_lowest_grade_names(students: List[Tuple[str, float]]) -> None:
    """
    Prints the names of students with the second lowest grade.
    """
    second_lowest_grade = get_second_lowest_grade(students)
    if second_lowest_grade is not None:
        names = get_students_with_grade(students, second_lowest_grade)
        for name in sorted(names):
            print(name)
    else:
        print("Not enough unique grades to determine the second lowest grade.")


def get_second_lowest_grade(students: List[Tuple[str, float]]) -> Optional[float]:
    """
    Returns the second lowest grade from the list of students.
    """
    unique_grades = sorted(set(score for _, score in students))
    return unique_grades[1] if len(unique_grades) > 1 else None


def get_students_with_grade(students: List[Tuple[str, float]], grade: float) -> List[str]:
    """
    Returns a list of student names who have the specified grade.
    """
    return [name for name, score in students if score == grade]


def main() -> None:
    """
    Main function to read student data and print names with the second lowest grade.
    """
    students: List[Tuple[str, float]] = []
    try:
        num_students = int(input("Enter number of students: "))
        for _ in range(num_students):
            name = input("Enter student name: ")
            score = float(input("Enter student score: "))
            students.append((name, score))
        print_second_lowest_grade_names(students)
    except ValueError:
        print("Invalid input. Please enter numeric values for number of students and scores.")


if __name__ == "__main__":
    main()
