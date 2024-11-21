# def fibbonacci():
#     saved_data= [1,1]
#     def inner(n):
#         if not isinstance(n, int):
#             raise TypeError
#         if n<0:
#             raise ValueError
#         while len(saved_data)<=n:
#             saved_data.append(saved_data[-2]+saved_data[-1])
#         return saved_data[n]
#     return inner

# f = fibbonacci()
# print(f(10))

# for i in range(10):
#     print(f(i))

# def is_int_args(func):
#     def wrapper(*args, **kwargs):
#         if not all(isinstance(arg, int) for arg in args):
#             raise TypeError("all arguments must be integers")

#         if not all(isinstance(arg, int) for arg in kwargs.values()):
#             raise TypeError("all arguments must be integers")

#         return func(*args, **kwargs)

#     return wrapper

# @is_int_args
# def is_positiv_args(func):
#     def wrapper(*args, **kwargs):
#         if not all(arg>0 for arg in args):
#             raise TypeError("all arguments must be positiv")

#         if not all(arg>0 for arg in kwargs.values()):
#             raise TypeError("all arguments must be positiv")

#         return func(*args, **kwargs)

#     return wrapper

# @is_positiv_args
# def add(a, b):
#     return a + b

# @is_positiv_args
# def sub(a, b):
#     return a - b

# @is_positiv_args
# def avg(*args):
#     return sum(args) / len(args)


# print(add(1, 2))
# print(sub(1, 2))
# print(avg(1, 2, 3, 4, 5))

class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def price(self):
        return self.__price * 1.2

    @price.setter
    def price(self, value):
        if not isinstance(value, int | float):
            raise TypeError("Price must be a number")
        if value <= 0:
            raise ValueError("Price must be greater than 0")
        self.__price = value

    @price.deleter
    def price(self):
        raise AttributeError("You can't delete price")
    
    @property
    def name(self):
        return str.upper(self.__name)
    
    @name.setter
    def name(self, value):
        if len(value)>=2:
            self.__name=value
        else:
            raise ValueError("Name is too short")
    @name.deleter
    def name(self):
        raise AttributeError("Name can't be deleted")
    def __str__(self):
        return f"{self.name} - {self.price}"
x = Product("Apple", 10)
print(x.name)
x.name = "sdfjjsn"
print(x)
# del x.name