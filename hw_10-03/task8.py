import string
myString=input("input: ")
for item in string.punctuation:
    myString = myString.replace(item, ' ')
while '  ' in myString:
    myString = myString.replace('  ', ' ')
words= myString.split(" ")
maxLength=len(words[0])
ind=[]
mIndex=0
for i in range (len(words)):
    ind.append(len(words[i]))
    if len(words[i])>maxLength:
       mIndex=i
       maxLength=len(words[i])
print(words[mIndex])
print(ind)