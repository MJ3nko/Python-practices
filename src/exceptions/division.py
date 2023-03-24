test_cases = int(input())

for case in range(test_cases):
    try:
        a, b = input().split()
        print(int(a) // int(b))
    except ZeroDivisionError as ze:
        print(f"Error Code: {ze}")
    except ValueError as ve:
        print(f"Error Code: {ve}")
