text1= set(input("text 1: ").split(" "))
text2 = set(input ("text 2: ").split(" "))
print(max(text1&text2, key=len))