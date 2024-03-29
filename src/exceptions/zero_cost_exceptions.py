import datetime


def troubling_method(x: str) -> int:
    # print(f"We will take a shot at converting {x}")

    try:
        return int(x)
    except ValueError as ve:
        print(f"Oh no, it couldn't be converted because of values: {ve}")
    except NotImplementedError:
        print("Somehow not implemented?")
    except Exception as ex:
        print(f"We have no idea: {ex}")

    # print("There was some kind of error")
    return -1


def main():
    print(troubling_method("77"))
    print(troubling_method(902))
    print(troubling_method("Nine hundred"))

    times = 10_000_000
    t0 = datetime.datetime.now()

    for _ in range(times):
        troubling_method("77")

    t1 = datetime.datetime.now()
    dt = t1 - t0
    print(f"Done in {dt.total_seconds()* 1000:,.2f} ms")


if __name__ == "__main__":
    main()
