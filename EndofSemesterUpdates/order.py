# order.py - Order class that depends on an external PaymentGateway

class PaymentGateway:
    def process_payment(self, amount):
        # Imagine this method connects to an external payment service
        pass

class Order:
    def __init__(self, amount):
        self.amount = amount
        self.payment_gateway = PaymentGateway()

    def pay(self):
        return self.payment_gateway.process_payment(self.amount)
