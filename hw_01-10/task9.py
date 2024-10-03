x=[]
while len(x)<12:
    temp = list(map(int, input('Зарплата за наступні місяці (через кому) ').split(",")))
    for i in temp:
        x.append(i)
print(x)
print (sum(x)/len(x))
