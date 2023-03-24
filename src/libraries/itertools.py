from itertools import product


def return_product(a, b):
    cartesian_product = product(a, b)
    return list(cartesian_product)


def main():
    a = input().split(sep=" ")
    b = input().split(sep=" ")

    results = return_product(a, b)
    for result in results:
        print(str(result).replace("'", ""), end=" ")


if __name__ == "__main__":
    main()
