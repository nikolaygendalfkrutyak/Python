import string
myString = input("Input: ")
for item in string.punctuation:
    myString = myString.replace(item, ' ')
while '  ' in myString:
    myString = myString.replace('  ', ' ')
words= myString.split(" ")
print (words)
print(len(words))