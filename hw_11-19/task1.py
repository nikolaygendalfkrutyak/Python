def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before func")
        value = func(*args, **kwargs)
        print ("after func")
        return value
    return wrapper

@decorator
def my_func():
    print("Functioooon")

my_func()