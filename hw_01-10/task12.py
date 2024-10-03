def isP(x):
    res = True
    i=2
    while i*i<=x:
       if not x%i:
           res=False
       i+=1
    return res
p = []
for i in range(99):
    if(isP(i+2)):
        p.append(i+2)
print(p)
print(len(p))