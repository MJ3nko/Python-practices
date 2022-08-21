def top_mat(n, m):
    lines = int((n - 1) / 2)
    minus_count = int((m - 3) / 2)
    for index in range(0, lines):
        middle_sign = ".|." * index
        outer_sign = "-" * minus_count
        print(f"{outer_sign}{middle_sign}.|.{middle_sign}{outer_sign}")
        minus_count -= 3


def welcome_line(m):
    side_text = "-" * int((m - 7) / 2)
    print(f"{side_text}WELCOME{side_text}")


def bottom_mat(n, m):
    lines = int((n - 1) / 2)
    middle_sign_count = int((m - 6) / 3)
    for index in range(1, lines + 1):
        middle_sign = ".|." * middle_sign_count
        outer_sign = "-" * (index * 3)
        print(f"{outer_sign}{middle_sign}{outer_sign}")
        middle_sign_count -= 2


def main():
    n, m = input().split(" ")
    n = int(n)
    m = int(m)
    top_mat(n, m)
    welcome_line(m)
    bottom_mat(n, m)


if __name__ == "__main__":
    main()
