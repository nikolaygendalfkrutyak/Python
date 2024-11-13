def primes(n):
    if not isinstance (n, int):
        raise TypeError("Hey man I really need an integer here")
    if n<2:
        raise ValueError("Prime numbers start at '2'")
    yield 2
    for i in range(3, n, 2):
        if is_prime(i):
            yield i
def is_prime(i):
    if i==2:
        return True
    k=3
    while k*k<=i:
        if not i%k:
            return False
        k+=1
    return True
print(" ".join(map(str, primes(100))))