class PositivityError(Exception):
    def __init__(self, message):
        super().__init__(message)

class Product:
    """
    Describes a product with a name and a price.
    """
    def __init__(self, name, price: float | int):
        """
        Initializes a product with a name and a price.
        :param name: name of the product
        :param price: price of the product
        """
        try:
            self.price = float(price)    
        except ValueError:
            raise TypeError("price must be a number")
        else:
            if price<=0:
                raise PositivityError("Price must be positiv")
        if not name:
            raise ValueError("name cannot be empty")
        self.name = name

    def __str__(self):
        return f"{self.name}: {self.price}"


class Cart:
    """
    Describes a cart with products.
    """
    def check_amount(quantity):
        try:
            quantity = float(quantity)    
        except ValueError:
            raise TypeError("Anknown amount of products")
        else:
            if quantity<=0:
                raise PositivityError("Amount must be positiv")
    def __init__(self):
        self.__products = {}

    def add_product(self, product: Product, quantity: int | float = 1):
        """
        Adds a product to the cart.
        :param product: instance of the Product class
        :param quantity: quantity of the product
        :return: None
        """
        if (not isinstance(product, Product)):
            raise TypeError("You can only add Products to the cart")
        self.check_amount(quantity)
        self.__products[product] = self.__products.get(product, 0) + quantity

    
    def remove_product(self, product: Product, quantity: int | float = 1):
        """
        Removes a product from the cart.
        :param product: instance of the Product class
        :param quantity: quantity of the product
        :return: None
        """
        self.check_amount(quantity)
        if product in self.__products:
            self.__products[product] -= quantity
            if self.__products[product] <= 0:
                del self.__products[product]

    def total(self):
        """
        Calculates the total price of the products in the cart.
        :return: total price of the products in the cart
        """
        return sum(product.price * quantity for product, quantity in self.__products.items())

    def __str__(self):
        res = '\n'.join(f"{product.name}: {quantity} x {product.price} UAH = {quantity * product.price} UAH"
                        for product, quantity in self.__products.items())
        return f"Cart:\n{res}\nTotal: {self.total()} UAH"
    
class PaymentProcessor():
    def __init__(self, cart):
        self.cart=cart
    def pay(self):
        return self.cart.total()

class CreditCardProcessor(PaymentProcessor):
    def __init__(self, cart):
        super().__init__(cart)
    def pay(self):
        return super().pay()+5
class PayPalPaymentProcessor(PaymentProcessor):
    def __init__(self, cart):
        super().__init__(cart)
    def pay(self):
        return super().pay()*1.1
class BankTransferProcessor(PaymentProcessor):
    def __init__(self, cart):
        super().__init__(cart)
    def pay(self):
        return super().pay()-0.1
               

pr1 = Product("Bread", 10)
pr2 = Product("Milk", 15)
pr3 = Product("Butter", 20)
cart = Cart()
cart.add_product(pr1)
cart.add_product(pr2, 2)
cart.add_product(pr3, 3)

# payment = PaymentProcessor(cart)
# payment_bank =  BankTransferProcessor(cart)
# payment_pay_pal = PayPalPaymentProcessor(cart)
# payment_card =  CreditCardProcessor(cart)
# print(payment.pay())
# print(payment_card.pay())
# print(payment_bank.pay())
# print(payment_pay_pal.pay())