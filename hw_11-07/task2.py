def geometrical_progression(b1, q, n):
    if not (isinstance (b1, int|float) and isinstance(q, int|float) and isinstance(n, int)):
        raise TypeError("Progression can be built only with numbers")
    for _ in range(n):
        yield b1
        b1*=q
        
for i in geometrical_progression(3, 2, 10):
    print(i)