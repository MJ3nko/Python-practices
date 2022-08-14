import time


def print_current_time():
    print(f"Current time: {time.ctime()}")


def print_current_time_in_milliseconds():
    print(f"Time in milliseconds: {str(time.time_ns())}")


if __name__ == "__main__":
    print_current_time()
    print_current_time_in_milliseconds()
