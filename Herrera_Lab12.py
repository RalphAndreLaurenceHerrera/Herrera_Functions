def display_menu():
    # Display the menu
    menu = {
        1: {"name": "Burger", "price": 50},
        2: {"name": "Pizza", "price": 100},
        3: {"name": "Pasta", "price": 70},
        4: {"name": "Fries", "price": 40},
        5: {"name": "Drink", "price": 30},
    }
    print("\n--- Food Menu ---")
    for key, item in menu.items():
        print(f"{key}. {item['name']} - PHP {item['price']}")
    return menu

def get_order(menu):
    # Take the user's order
    while True:
        try:
            choice = int(input("\nEnter the item number you want to order: "))
            if choice in menu:
                quantity = int(input(f"How many {menu[choice]['name']}s would you like? "))
                if quantity > 0:
                    return menu[choice], quantity
                else:
                    print("Please enter a valid quantity!")
            else:
                print("Invalid item number. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

def process_payment(total_cost):
    # Process the payment
    while True:
        try:
            cash = float(input(f"Your total is PHP {total_cost}. Enter cash amount: "))
            if cash >= total_cost:
                return cash
            else:
                print(f"Insufficient amount, please try again. Note: You need at least PHP {total_cost}.")
        except ValueError:
            print("Please enter a valid amount of cash.")

def main():
    menu = display_menu()
    item, quantity = get_order(menu)
    total_cost = item['price'] * quantity
    cash = process_payment(total_cost)
    change = cash - total_cost

    # Receipt
    print("\n---User's Receipt ---")
    print(f"Item: {item['name']}")
    print(f"Quantity: {quantity} {item['name']}")
    print(f"Total Cost: PHP {total_cost}")
    print(f"Cash Rendered: PHP {cash}")
    print(f"Change: PHP {change:.2f}")
    print("\nThank you for ordering! Have a great day!")

if __name__ == "__main__":
    main()