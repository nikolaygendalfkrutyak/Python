from mods.products import Product
from mods.cart import Cart
from mods.payment import BankTransferProcessor, PayPalPaymentProcessor, CreditCardProcessor
try:
    pr1 = Product("Bread", 10)
    pr2 = Product("Milk", 15)
    pr3 = Product("Butter", 20)
    cart = Cart()
    cart.add_product(pr1)
    cart.add_product(pr2, -2) # Error to be fixed))
    cart.add_product(pr3, 3)
except Exception as e:
    print(e)
else:
    payment_bank =  BankTransferProcessor(cart)
    payment_pay_pal = PayPalPaymentProcessor(cart)
    payment_card =  CreditCardProcessor(cart)
    print(payment_card.pay())
    print(payment_bank.pay())
    print(payment_pay_pal.pay())
