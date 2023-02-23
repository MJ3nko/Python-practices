def distinct_countries(n):
    countries = set()
    distinct_countries = 0
    for _ in range(n):
        country = input()
        if country not in countries:
            distinct_countries += 1
            countries.add(country)
    return distinct_countries


if __name__ == "__main__":
    n = int(input())
    result = distinct_countries(n)
    print(result)
