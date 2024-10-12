text=input("Text: ")
betterText=set(text.split(" "))
ans=[]
for i in betterText:
    if text.count(i)==1:
        ans.append(i)
print(len(ans))
