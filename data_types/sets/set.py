def average(array: list) -> float:
    sum = 0
    array = set(array)
    for element in array:
        sum += element
    average = f"{sum / len(array):0.3f}"
    return average


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
