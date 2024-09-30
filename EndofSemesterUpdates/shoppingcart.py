class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}: {self.quantity} @ ${self.price:.2f}"

class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        for p in self.products:
            if p.name == product.name:
                p.quantity += product.quantity
                return
        self.products.append(product)

    def remove_product(self, product_name):
        self.products = [p for p in self.products if p.name != product_name]

    def update_quantity(self, product_name, quantity):
        for p in self.products:
            if p.name == product_name:
                p.quantity = quantity
                return

    def calculate_total(self):
        return sum(p.price * p.quantity for p in self.products)

    def list_products(self):
        return [str(p) for p in self.products]
