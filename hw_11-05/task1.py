from mods.products import Product
from mods.cart import Cart
from mods.payment import BankTransferProcessor, PayPalPaymentProcessor, CreditCardProcessor
# try:
pr1 = Product("Bread", 10)
pr2 = Product("Milk", 15)
pr3 = Product("Butter", 20)
cart1 = Cart("Cart 1")
cart2 = Cart("Cart 2")
cart1.add_product(pr1)
cart1.add_product(pr2, 2)
cart1.add_product(pr3, 3)
cart2+=pr2
cart2.add_product(pr3, 3)
print (cart1)
# cart1+= pr2 * 10 #Wanted to create Cart by myltiplying the product but faced circular import. 
cart1+=cart2
print (cart1)
# except Exception as e:
#     print(e)
# else:
#     payment_bank =  BankTransferProcessor(cart)
#     payment_pay_pal = PayPalPaymentProcessor(cart)
#     payment_card =  CreditCardProcessor(cart)
#     print(payment_card.pay())
#     print(payment_bank.pay())
#     print(payment_pay_pal.pay())
