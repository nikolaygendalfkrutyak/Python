from mods.logs import lg_products
from mods.my_exc import PositivityError
from mods.products import Product
class Cart:
    """
    Describes a cart with products.
    """
    def check_amount(self, quantity):
        if not isinstance(quantity, float|int):
            lg_products.debug("Amount must be a number")
            raise TypeError("Anknown amount of products")
        if quantity<=0:
            lg_products.debug("Amount must be positiv")
            raise PositivityError("Amount must be positiv")
    def __init__(self, name):
        self.__name = name
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
        res ='\n'.join(f"{product.name}: {quantity} x {product.price} UAH = {quantity * product.price} UAH"
                        for product, quantity in self.__products.items())
        return f"Cart - {self.__name}:\n{res}\nTotal: {self.total()} UAH \n"
    
    def __add__(self, other):
        if isinstance(other, Product):
            return (self.add_product(other))
        return NotImplemented
    
    
    def __iadd__(self, other):
        if isinstance (other, Product):
            self.add_product(other)
            return self
        if isinstance(other, Cart):
            for product, quantity in other.__products.items():
                self.add_product(product, quantity)
            return self
        return NotImplemented
    