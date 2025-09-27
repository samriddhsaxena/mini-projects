menu = {
    "Pizza": 80,
    "Burger": 120,
    "Pasta": 100,
    "Fries": 50,
    "Salad": 60
}

print("Welcome to PYTHON Restaurant")
print("Pizza: Rs80\nBurger: Rs120\nPasta: Rs100\nFries: Rs50\nSalad: Rs60\n")

order_total = 0

item_1 = input("Enter name of item you want to order: ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item is {item_1} has been added to your order.")
else:
    print("Item not found in menu.")
    exit()
    
while True:
    another_item = input("Do you want to order another item? (yes/no): ")
    if another_item == "yes":
        item_2 = input("Enter name of item you want to order: ")
        if item_2 in menu:
            order_total += menu[item_2]
            print(f"Your item is {item_2} has been added to your order.")
        else:
            print("Item not found in menu.")
            break
    else:
        break

print("Your order total is Rs", order_total)