myString = input("input: ")
myLength = len(myString)
for i in range(1, myLength):
    if not myLength%i:  
        if myString[:i]*(myLength//i)==myString:
            print(myString[:i])
            break
else:
    print("There is no pattern")