from mods.logs import lg_products
class PaymentProcessor():
    def __init__(self, cart):
        self.cart=cart
    def pay(self):
        return self.cart.total()

class CreditCardProcessor(PaymentProcessor):
    def __init__(self, cart):
        super().__init__(cart)
    def pay(self):
        lg_products.info("payment was made")
        return super().pay()+5
class PayPalPaymentProcessor(PaymentProcessor):
    def __init__(self, cart):
        super().__init__(cart)
    def pay(self):
        lg_products.info("payment was made")
        return super().pay()*1.1
class BankTransferProcessor(PaymentProcessor):
    def __init__(self, cart):
        super().__init__(cart)
    def pay(self):
        lg_products.info("payment was made")
        return super().pay()-0.1