import timeit
import math


def f_to_c(f: float) -> float:
    """Convert Fahrenheit to Celsius."""
    return (f - 32) * 5 / 9


def c_to_f(c: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return c * 9 / 5 + 32


TEST_VALUES = [-459.67, -273.15, 0.0, 32.0, 42.0, 273.15, 100.0, 212.0, 373.15]


def test_conversions() -> None:
    for t in TEST_VALUES:
        assert_round_trip(t)


def test_speed():
    count = int(1_000_000 / len(TEST_VALUES))
    for _ in range(count):
        for t in TEST_VALUES:
            round_trip(t)


def round_trip(t: float) -> float:
    return f_to_c(c_to_f(t))


def assert_round_trip(t: float) -> None:
    # Round-trip Fahrenheit through Celsius:
    assert math.isclose(t, f_to_c(c_to_f(t))), f"{t} F -> C -> F failed!"
    print(f"{t:,.1f} F -> {f_to_c(t):,.1f} C")
    # Round-trip Celsius through Fahrenheit:
    assert math.isclose(t, c_to_f(f_to_c(t))), f"{t} C -> F -> C failed!"
    t2 = f_to_c(t)
    print(f"{t2:,.1f} C -> {c_to_f(t2):,.1f} F")
    print()


if __name__ == "__main__":
    test_conversions()

    duration = timeit.timeit("test_speed()", globals=globals(), number=1)
    print(f"Done in {duration * 1000:.2f} ms")
