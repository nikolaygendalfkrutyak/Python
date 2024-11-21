def limit_calls(max_calls):
    cash = {"calls" : 0}
    def decorator(func):
        def wrapper(*args, **kwargs):
            if cash["calls"]<max_calls:
                cash["calls"]+=1
                value = func(*args, **kwargs)
                return value
        
        return wrapper
    return decorator

@limit_calls(4)
def my_func():
    print("Functioooon")

for _ in range(10):
    my_func()