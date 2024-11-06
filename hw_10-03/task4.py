import string
myName = input("Name: ")
allNames = myName.split(" ")
validity = True
for i in allNames:
    for j in string.punctuation:
        if j in i:
            validity = False
    for q in range(10):
        if str(q) in i:
            validity = False
    if not (i[0].isupper or i[1:].islower):
        validity=False
if validity:
    print (f"{myName} is a normal name")
else:
    print(f"{myName} is not a name")