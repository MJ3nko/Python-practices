import time


def print_current_time():
    current_time = time.ctime()
    print(f"Current time: {current_time}")


def print_current_time_in_milliseconds():
    milliseconds = str(time.time_ns())
    print(f"Time in milliseconds: {milliseconds}")


def main():
    print_current_time()
    print_current_time_in_milliseconds()


if __name__ == "__main__":
    main()
