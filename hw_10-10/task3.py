text={"a":1, "b":2, "c":3, "d":3}
values=set(text.values())
ans=[]
if len(values)==len(text):
    print("Всі значення унікальні")
else:
    print("Не всі значення унікальні")