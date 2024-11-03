"""
        module products consits of class products 
        which helps to create different products
        And class Carts, which is made to collect carts to be able to "buy" them
"""
from mods.logs import lg_products
from mods.my_exc import PositivityError
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
        if not isinstance(price, float|int):
            lg_products.debug("price must be a number")
            raise TypeError("price must be a number")
        if price<=0:
            lg_products.debug("Price must be positiv")
            raise PositivityError("Price must be positiv")
        self.price = price
        if not name:
            raise ValueError("name cannot be empty")
        self.name = name
        

    def __str__(self):
        return f"{self.name}: {self.price}"



