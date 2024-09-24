# test_order.py - Unit tests for the Order class using mocking

import unittest
from unittest.mock import Mock
from order import Order, PaymentGateway

class TestOrder(unittest.TestCase):
    
    def setUp(self):
        """Set up an Order object for testing."""
        self.order = Order(100)
        self.order.payment_gateway = Mock(spec=PaymentGateway)

    def test_pay_success(self):
        """Test that payment is processed successfully."""
        self.order.payment_gateway.process_payment.return_value = True
        result = self.order.pay()
        self.order.payment_gateway.process_payment.assert_called_with(100)
        self.assertTrue(result)

    def test_pay_failure(self):
        """Test that payment fails."""
        self.order.payment_gateway.process_payment.return_value = False
        result = self.order.pay()
        self.order.payment_gateway.process_payment.assert_called_with(100)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
