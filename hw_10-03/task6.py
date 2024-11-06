import string
myString = input("Input: ")
for item in string.punctuation:
    myString = myString.replace(item, ' ')
while '  ' in myString:
    myString = myString.replace('  ', ' ')
words= myString.split(" ")
nu = [1]*len(words)
for i in range(len(words)):
    count=0
    for j in range(len(words)):
        if words[i]==words[j]:
            count+=1
    nu[i]=count
print(words)
print(nu)
    