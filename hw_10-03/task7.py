import string
myString = input("Input: ")
for i in string.punctuation:
    myString=myString.replace(i," ")
while ' ' in myString:
    myString = myString.replace(' ', '')
print(myString)