text1=set(input("Text1: ").split(" "))
text2=set(input("Text2: ").split(" "))
text3=set(input("Text2: ").split(" "))
print ((text1 & text2)| (text2 &text3) | (text3 & text1))