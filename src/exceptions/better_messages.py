from collections import namedtuple

Thing = namedtuple("Thing", "name, weight, speed")


def func1(a, b, c, d, e):
    return a.get(b).get(c).get(d).get(e).strip().upper()


def func2(thing1, thing2, thing3):
    return thing1.weight + thing2.weight + thing3.weight


def main():
    data = {
        "region": {
            "country": {
                "size": {
                    "area": 1_000_000,
                    "units": "miles",
                }
            }
        }
    }

    b = "region"
    c = "country"
    d = "size"
    e = "units"

    print(func1(data, b, c, d, e))

    # d = "bigness"
    # print(func1(data, b, c, d, e))
    #
    # File "Python-practices\src\exceptions\better_messages.py", line 7, in func1
    # return a.get(b).get(c).get(d).get(e).strip().upper()
    #        ^^^^^^^^^^^^^^^^^^^^^^^^^^
    # AttributeError: 'NoneType' object has no attribute 'get'

    t1 = Thing("Bob", 70, 24)
    t2 = Thing("Sarah", 65, 32)
    t3 = Thing("Jake", 72, 20)

    total_weight = func2(t1, t2, t3)
    print(f"The total weight is {total_weight} kg")

    # t2 = None
    # total_weight = func2(t1, t2, t3)
    # print(f"The total weight is {total_weight} kg")
    #
    # return thing1.weight + thing2.weight + thing3.weight
    #                        ^^^^^^^^^^^^^
    # AttributeError: 'NoneType' object has no attribute 'weight'


if __name__ == "__main__":
    main()
