myString=input("input: ")
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for j in range(len(alphabet)):
    myString = myString.replace(alphabet[j], f"{j+1}_")
print(myString)
