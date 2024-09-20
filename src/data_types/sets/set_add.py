def count_distinct_countries(num_countries: int) -> int:
    countries: set[str] = set()
    for _ in range(num_countries):
        country: str = input("Enter country name: ")
        countries.add(country)
    return len(countries)


if __name__ == "__main__":
    num_countries: int = int(input("Enter the number of countries: "))
    distinct_count: int = count_distinct_countries(num_countries)
    print(f"Number of distinct countries: {distinct_count}")
