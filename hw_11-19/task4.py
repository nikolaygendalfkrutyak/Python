import time
def decorator(func):
    def wrapper(*args, **kwargs):
        start_time=time.time()       
        value = func(*args, **kwargs)
        end_time=time.time()
        print(end_time-start_time) 
        return value
    return wrapper

@decorator
def my_func():
    time.sleep(2)

my_func()