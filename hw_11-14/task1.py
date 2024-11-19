def generators_decorator(func):
    def my_gen(first, n):
        a = list(func(first, n))
        for i in a:
            yield i
        
    return my_gen

def arif_prog(first, count, step=1):
    for _ in range(count):
            yield first
            first+=step

def geom_prog(first, count, step=2):
    for _ in range(count):
            yield first
            first*=step


a_func = generators_decorator(arif_prog)
b_func = generators_decorator(geom_prog)

print(" ".join(map(str, a_func(5, 20))))
print(" ".join(map(str, b_func(5, 20))))