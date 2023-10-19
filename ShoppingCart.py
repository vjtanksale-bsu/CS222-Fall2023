import unittest

class ShoppingCart:
    def __init__(self):
        self.items = []
    def AddItem(self, product, quantity = 1):
        self.items.append({'product': product, 'quantity': quantity})
    def RemoveItem(self, product, quantity = 1):
        for item in self.items:
            if item['product'] == product:
                item['quantity'] -= quantity
                if item['quantity'] <= 0:
                    self.items.remove(item)
    def CalculateTotal(self):
        total = sum(item['product'].price * item['quantity'] for item in self.items)
        return total
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
class TestShoppingCart(unittest.TestCase):
    def setUp(self) -> None:
        self.cart = ShoppingCart()
        self.product0 = Product("Phone", 1000)
        self.product1 = Product("Computer", 2000)
    def test_AddItem(self):
        self.cart.AddItem(self.product0, 2)
        self.assertEqual(len(self.cart.items), 1)
    def test_RemoveItem(self):
        self.cart.AddItem(self.product0, 5)
        self.cart.RemoveItem(self.product0, 2)
        self.assertEqual(self.cart.items[0]['quantity'], 3)
    def test_CalculateTotal(self):
        self.cart.AddItem(self.product0, 2)
        self.cart.AddItem(self.product1, 5)
        total = self.cart.CalculateTotal()
        self.assertEqual(total, 12000)

if __name__ == "__main__":
    unittest.main()
