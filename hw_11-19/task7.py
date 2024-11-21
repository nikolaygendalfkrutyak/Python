def casher(func):
    buffer = {
        0: 0,
        1: 1,
    }
    def inner(n):
        if n in buffer:
            print ("Result from buffer:")
            return buffer[n]
        buffer[n]=func(n)
        print("Result of function:")
        return buffer[n]

    return inner
@casher
def fibonacci(n):
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a + b
    return a
print(fibonacci(10))
print(fibonacci(10))
