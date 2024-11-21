def decorator(func):
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        file = open('text.txt', 'a')
        file.write(f"{value} \n")
        file.close()
        return value
    return wrapper

@decorator
def my_func():
    return(1)

my_func()