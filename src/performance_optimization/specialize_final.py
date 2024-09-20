import datetime
import math

def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32.0) * (5 / 9)

def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return celsius * (9 / 5) + 32.0

TEST_TEMPERATURES = [-459.67, -273.15, 0.0, 32.0, 42.0, 273.15, 100.0, 212.0, 373.15]

def test_conversions() -> None:
    """Test the conversion functions with predefined values."""
    for temperature in TEST_TEMPERATURES:
        assert_conversion_round_trip(temperature)

def test_speed() -> None:
    """Test the speed of the conversion functions."""
    iterations = int(1_000_000 / len(TEST_TEMPERATURES))
    for _ in range(iterations):
        for temperature in TEST_TEMPERATURES:
            perform_round_trip(temperature)

def perform_round_trip(temperature: float) -> float:
    """Perform a round-trip conversion from Fahrenheit to Celsius and back."""
    return fahrenheit_to_celsius(celsius_to_fahrenheit(temperature))

def assert_conversion_round_trip(temperature: float) -> None:
    """Assert that the round-trip conversion maintains the original value."""
    # Round-trip Fahrenheit through Celsius:
    fahrenheit_to_celsius_result = fahrenheit_to_celsius(temperature)
    celsius_to_fahrenheit_result = celsius_to_fahrenheit(temperature)
    assert math.isclose(temperature, fahrenheit_to_celsius_result), f"{temperature} F -> C -> F failed!"
    print(f'{temperature:,.1f} F -> {fahrenheit_to_celsius_result:,.1f} C')
    
    # Round-trip Celsius through Fahrenheit:
    assert math.isclose(temperature, celsius_to_fahrenheit_result), f"{temperature} C -> F -> C failed!"
    print(f'{fahrenheit_to_celsius_result:,.1f} C -> {celsius_to_fahrenheit_result:,.1f} F')
    print()

if __name__ == "__main__":
    start_time = datetime.datetime.now()

    # Uncomment to run conversion tests
    # test_conversions()
    
    test_speed()

    end_time = datetime.datetime.now()
    duration = end_time - start_time
    print(f'Done in {duration.total_seconds() * 1000:.2f} ms')
