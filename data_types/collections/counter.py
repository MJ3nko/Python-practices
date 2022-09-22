from collections import Counter


def return_profits(shoes_inventory: Counter, customers: int):
    profit = 0
    for _ in range(customers):
        order = input().split(" ")
        shoe_size = int(order[0])
        shoe_price = int(order[1])
        if is_size_available(shoe_size, shoes_inventory):
            profit += shoe_price
    return profit


def is_size_available(shoe_size: int, shoes_inventory: Counter) -> bool:
    if shoe_size in shoes_inventory.keys():
        shoes_inventory[shoe_size] -= 1
        if shoes_inventory[shoe_size] == 0:
            del (shoes_inventory[shoe_size])
        return True
    return False


def main():
    _ = int(input())
    shoes_inventory = Counter(list(map(int, input().split(" "))))
    customers = int(input())
    money = return_profits(shoes_inventory, customers)
    print(money)


if __name__ == "__main__":
    main()
