from collections import Counter


def return_profits(shoes_inventory: Counter, customers: int) -> int:
    profit = 0
    for _ in range(customers):
        shoe_size, shoe_price = map(int, input().split())
        if shoes_inventory[shoe_size] > 0:
            profit += shoe_price
            shoes_inventory[shoe_size] -= 1
            if shoes_inventory[shoe_size] == 0:
                del shoes_inventory[shoe_size]
    return profit


def main():
    _ = int(input())
    shoes_inventory = Counter(map(int, input().split()))
    customers = int(input())
    money = return_profits(shoes_inventory, customers)
    print(money)


if __name__ == "__main__":
    main()
