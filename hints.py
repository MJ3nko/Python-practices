def type_hint(name: str) -> str:
    # Make code more readable.
    # Python 3.5+
    print(f"Hello {name}")


def readability():
    # Improve readability of large numbers.
    # Python 3.6+
    x = 1_000_000
    y = 1000000
    print(x, y, x == y)


type_hint("Anonymous")
readability()
