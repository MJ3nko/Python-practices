def polynomial(x_k, p):
    x = int(x_k[0])
    k = int(x_k[1])
    result = poly_sum(int(x), p)
    if result == k:
        return True
    return False


def poly_sum(x, p):
    result = 0
    operation = ""
    for word in p:
        if "*x**" in word:
            times = int(word.split("*x**")[0])
            potenca = int(word.split("*x**")[1])
            number = times * (x ** int(potenca))
            result = execute_operation(result, operation, number)
        elif "**" in word:
            potenca = int(word.split("**")[1])
            number = x**potenca
            result = execute_operation(result, operation, number)
        elif word in ["+", "-", "*", "/"]:
            operation = word
        elif len(word) == 1:
            if "x" in word:
                number = x
                result = execute_operation(result, operation, number)
            else:
                number = int(word)
                result = execute_operation(result, operation, number)
    return result


def execute_operation(result, operation, number):
    if operation == "+" or operation == "":
        result += number
    elif operation == "-":
        result -= number
    elif operation == "*":
        result *= number
    elif operation == "/":
        result /= number
    return result


def main():
    x_k = input().split(sep=" ")
    p = input().split(sep=" ")
    statement = polynomial(x_k, p)
    if statement:
        print(True)
    else:
        print(False)


if __name__ == "__main__":
    main()
