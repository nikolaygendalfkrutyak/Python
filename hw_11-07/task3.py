def my_range(n, end=None, step=None):
    
    if not (isinstance (n, int) and isinstance(end, int|None) and isinstance(step, int|None)):
        raise TypeError("not each object can be interpreted as an integer")
    
    if not step or step==None:
        step = 1
    if not end or end==None:
        end =n
        n=0
    while (end-n)//step>0:
        yield n
        n+=step    

print(" ".join(map(str, my_range(1, 13, 3))))
print("And now built-in range")
print(" ".join(map(str, range(1, 13, 3))))