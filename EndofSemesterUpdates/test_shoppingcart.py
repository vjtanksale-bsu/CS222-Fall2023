import unittest
from shoppingcart import ShoppingCart, Item  # Import classes

class TestShoppingCart(unittest.TestCase):

    def setUp(self):
        self.cart = ShoppingCart()

    def test_add_item(self):
        item = Item("Apple", 1.0)
        self.cart.add_item(item)
        self.assertIn(item, self.cart.items)

    def test_remove_item(self):
        item = Item("Apple", 1.0)
        self.cart.add_item(item)
        self.cart.remove_item(item)
        self.assertNotIn(item, self.cart.items)

    def test_total_price(self):
        item1 = Item("Apple", 1.0)
        item2 = Item("Banana", 2.0)
        self.cart.add_item(item1)
        self.cart.add_item(item2)
        self.assertEqual(self.cart.total_price(), 3.0)

if __name__ == '__main__':
    unittest.main()
