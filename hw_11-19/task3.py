def decorator(func):
    def wrapper(*args, **kwargs):
        try:
            value = func(*args, **kwargs)
            return value
        except Exception as e:
            print (e)
            return None
    return wrapper

@decorator
def my_func():
    return(1/0)

my_func()