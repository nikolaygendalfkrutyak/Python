def is_palinrome(myString):
    try:
        for i in range(len(myString)//2):
            if(myString[i]!=myString[len(myString)-i-1]):
                return False
        return True
    except:
        return False
    
maxP = 0;
a, b = 100, 100
for i in range(100, 1000):
    for j in range(i, 1000):
        if is_palinrome(str(i*j)) and i*j >maxP:
            maxP=i*j
            a=i
            b=j
print (f"{a}*{b}={maxP}")