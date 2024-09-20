def average(array: list) -> float:
    unique_elements = set(array)
    total_sum = sum(unique_elements)
    average_value = total_sum / len(unique_elements)
    return round(average_value, 3)


if __name__ == "__main__":
    n = int(input("Enter the number of elements: "))
    arr = list(map(int, input("Enter the elements separated by space: ").split()))
    result = average(arr)
    print(f"{result:.3f}")
