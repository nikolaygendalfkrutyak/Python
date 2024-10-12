text=input("Text: ").split(" ")
betterText=set(text)
ans=[]
for i in betterText:
    if text.count(i)==1:
        ans.append(i)
print("Всі елементи унікальні" if len(ans)==len(text) else "Не всі елементи унікальні")