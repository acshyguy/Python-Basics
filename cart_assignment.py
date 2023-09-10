class Cart:

    def __init__(self, item_id, name, unit_price, quantity):
        self.item_id = item_id
        self.name = name
        self.unit_price = unit_price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.unit_price * self.quantity
    

items = [
    Cart(1, "Bread", 1.99, 3),
    Cart(2, "Biscuit", 0.99, 4),
    Cart(3, "Orange", 0.79, 2),
    Cart(4, "Ewagoin", 2.99, 1),
    Cart(5, "Beans", 1.49, 5),
    Cart(6, "File", 3.49, 2),
    Cart(7, "Rice", 4.99, 1),
    Cart(8, "Bic", 0.49, 6),
    Cart(9, "Pencil", 0.79, 3),
    Cart(10, "Eraser", 1.99, 2)
]

def display_items():
    print("Available Items:")
    print("ID\tName\t\tPrice\tQuantity")
    for item in items:
        print(f"{item.item_id}\t{item.name}\t\t${item.unit_price}\t{item.quantity}")



def calculate_cart_total(cart_items):
    total = 0
    for item in cart_items:
        total += item.calculate_total_price()
    return total

selected_items = []
display_items()

print(" ")

smiley = '\U0001F600'
while True:
    choice = input("Enter the item ID to add it to the cart (or 'q' to quit): ")
    if choice == 'q':
        break

    try:
        item_id = int(choice)
        item = next((item for item in items if item.item_id == item_id), None)
        if item:
            if item.quantity > 0:
                selected_items.append(item)
                print(f"{item.name} added to the cart.")
                item.quantity -= 1
            else:
                print(f"{item.name} is out of stock. OTILOR!!!" + smiley)
        else:
            print("Oops! Invalid item Id. Try again")

    except ValueError:
        print("Invalid input. Please try again.")

if selected_items:
    print("Items in your cart:")
    for item in selected_items:
        print(f"{item.name} - Quantity: {item.quantity}")
    total_price = calculate_cart_total(selected_items)
    print(f"Total price of the cart: ${total_price:.2f}")
else:
    print("No items selected.")

print("\n Remaining items and quantities: ")
print(display_items())