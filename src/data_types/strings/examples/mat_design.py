def print_top_mat(n, m):
    lines = (n - 1) // 2
    for i in range(lines):
        pattern = ".|." * (2 * i + 1)
        print(pattern.center(m, '-'))


def print_welcome_line(m):
    print("WELCOME".center(m, '-'))


def print_bottom_mat(n, m):
    lines = (n - 1) // 2
    for i in range(lines - 1, -1, -1):
        pattern = ".|." * (2 * i + 1)
        print(pattern.center(m, '-'))


def main():
    n, m = map(int, input().split())
    print_top_mat(n, m)
    print_welcome_line(m)
    print_bottom_mat(n, m)


if __name__ == "__main__":
    main()
