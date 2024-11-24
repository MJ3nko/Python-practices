def while_loop():
    """
    Continuously prompts the user for a value until 0 is entered.
    """
    while True:
        try:
            value = int(input("Enter a value (0 to exit): "))
            if value == 0:
                break
            print(f"Value {value}")
        except ValueError:
            print("Please enter a valid integer.")


def walrus_operator():
    """
    Continuously prompts the user for a value using the walrus operator
    until 0 is entered.
    """
    while (value := input("Enter a value (0 to exit): ")) != "0":
        try:
            value = int(value)
            print(f"Value {value}")
        except ValueError:
            print("Please enter a valid integer.")


def for_loop():
    """
    Demonstrates the use of a for loop with a throwaway variable
    and a range with a step.
    """
    for _ in range(1):
        print("Underscore is a throwaway variable.")

    for value in range(0, 10, 2):
        print(value)


def main():
    """
    Main function to run the examples.
    """
    while_loop()
    walrus_operator()
    for_loop()


if __name__ == "__main__":
    main()
