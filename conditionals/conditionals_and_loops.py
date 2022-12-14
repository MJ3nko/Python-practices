def while_loop():
    # Notice how we need to ask for a value twice.
    value = int(input("Enter a value: "))
    while value != "0":
        value = int(input("Enter a value: "))
        print(f"Value {value}")


def walrus_operator():
    # Let's use the WALRUS OPERATOR to avoid
    # having to ask for the value twice.
    # Python 3.8+
    while (value := input("Enter a value: ")) != "0":
        print(f"Value {value}")


def for_loop():
    for _ in range(1):
        print("Underscore is a throwaway variable.")

    for value in range(0, 10, 2):
        print(value)


def main():
    while_loop()
    walrus_operator()
    for_loop()


if __name__ == "__main__":
    main()
