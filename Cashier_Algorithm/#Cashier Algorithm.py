import random

def get_items():
    items = int(input("How many items do you have? "))
    return items

def calculate_total_price(num_items):
    total = 0
    for i in range(num_items):
        price = random.uniform(1, 10)
        print(f"Price of item {i+1}: ${price:.2f}")
        total += price
    return round(total, 2)

def calculate_change(amount_paid, total_price, denominations):
    change_amount = round(amount_paid - total_price, 2)
    print(f"\nTotal change: ${change_amount:.2f}")

    change = {}
    
    for denomination in denominations:
        if change_amount >= denomination:
            num_of_denomination = int(change_amount // denomination)
            change[denomination] = num_of_denomination
            change_amount -= num_of_denomination * denomination
    
    change_amount = round(change_amount, 2)
    if change_amount > 0:
        print(f"Remaining change cannot be given exactly: ${change_amount:.2f}")
    return change

def main():
    num_items = get_items()
    total_price = calculate_total_price(num_items)
    print(f"\nTotal price of items: ${total_price:.2f}")

    extra_amount = random.uniform(0, 10)
    amount_paid = round(total_price + extra_amount, 2)
    print(f"\nCustomer paid: ${amount_paid:.2f}")

    change_types = [100, 50, 20, 10, 5, 1, 0.25, 0.10, 0.05, 0.01] 
    change = calculate_change(amount_paid, total_price, change_types)

    if change:
        print("\nChange breakdown:")
        for denom, count in change.items():
            print(f"${denom:.2f}: {count} piece(s)")

if __name__ == "__main__":
    main()
