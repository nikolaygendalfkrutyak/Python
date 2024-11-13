class CartIterator:
    def __init__(self, products):
        self.products = products
        self.index = 0

    def __next__(self):
        if self.index < len(self.products):
            student = self.products[self.index]
            self.index += 1
            return student
        raise StopIteration


class Product:
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def __str__(self):
        return f"{self.name} costs {self.price} dollars."
    
    
class Cart:
    def __init__(self, name):
        self.name = name
        self.__products = {}

    def __iter__(self):
        return CartIterator(self.__products)

    def __len__(self):
        return len(self.products)

    def __getitem__(self, index):
        return self.products[index]

    def add_product(self, product: Product, quantity: int | float = 1):
        """
        Adds a product to the cart.
        :param product: instance of the Product class
        :param quantity: quantity of the product
        :return: None
        """
        if (not isinstance(product, Product)):
            raise TypeError("You can only add Products to the cart")
        self.__products[product] = self.__products.get(product, 0) + quantity
    
    def __str__(self):
        res ='\n'.join(f"{product.name}: {quantity} x {product.price} UAH = {quantity * product.price} UAH"
                        for product, quantity in self.__products.items())
        return f"Cart - {self.__name}:\n{res}\nTotal: {self.total()} UAH \n"

cart = Cart("My Cart")

cart.add_product(Product("Water", 1), 2)
cart.add_product(Product("Cola", 1.5), 110)
cart.add_product(Product("Beer", 2), 3)

for products in cart:
    print(products)

print(cart[0])
print(len(cart))

# def fibonacci(n):
#     a, b = 1, 1
#     for _ in range(n):
#         a, b = b, a + b
#         yield a


# print(" ".join(map(str, fibonacci(10))))
