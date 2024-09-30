import unittest
from shoppingcart import Product, ShoppingCart

class TestShoppingCart(unittest.TestCase):

    def setUp(self):
        self.cart = ShoppingCart()
        product = Product("Apple", 1.50, 3)
        self.cart.add_product(product)
        

    def test_add_product(self):
        self.assertEqual(len(self.cart.products), 1)
        self.assertEqual(self.cart.products[0].name, "Apple")

    def test_remove_product(self):
#        product = Product("Apple", 1.50, 3)
#        self.cart.add_product(product)
        self.cart.remove_product("Apple")
        self.assertEqual(len(self.cart.products), 0)

    def test_update_quantity(self):
#        product = Product("Apple", 1.50, 3)
#        self.cart.add_product(product)
        self.cart.update_quantity("Apple", 5)
        self.assertEqual(self.cart.products[0].quantity, 5)

    def test_calculate_total(self):
#        self.cart.add_product(Product("Apple", 1.50, 3))
        self.cart.add_product(Product("Banana", 0.75, 6))
        total = self.cart.calculate_total()
        self.assertEqual(total, 9.0)

    def test_list_products(self):
#        self.cart.add_product(Product("Apple", 1.50, 3))
        self.cart.add_product(Product("Banana", 0.75, 6))
        product_list = self.cart.list_products()
        self.assertEqual(len(product_list), 2)
        self.assertEqual(product_list[0], "Apple: 3 @ $1.50")

if __name__ == '__main__':
    unittest.main()
