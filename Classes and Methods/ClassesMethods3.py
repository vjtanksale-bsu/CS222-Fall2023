class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, quantity, price_per_item):
        if item_name in self.items:
            self.items[item_name]['quantity'] += quantity
        else:
            self.items[item_name] = {'quantity': quantity, 'price': price_per_item}

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]

    def calculate_total(self):
        total = 0
        for item_name, item_data in self.items.items():
            total += item_data['quantity'] * item_data['price']
        return total

    def print_receipt(self):
        print("Receipt:")
        for item_name, item_data in self.items.items():
            print(
                f"{item_name}: {item_data['quantity']} x ${item_data['price']} = "
                f"${item_data['quantity'] * item_data['price']}")
        print(f"Total: ${self.calculate_total()}")


# Create an instance of the ShoppingCart class
cart = ShoppingCart()

# Add items to the cart
cart.add_item("Apple", 5, 0.5)
cart.add_item("Banana", 3, 0.3)
cart.add_item("Orange", 2, 0.4)

# Remove an item from the cart
cart.remove_item("Banana")

# Print the receipt
cart.print_receipt()
