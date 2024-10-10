myString = input("input: ")
while "<" in myString:
    start = myString.find("<")
    end = myString.find(">")+1
    myString=myString[:start]+myString[end:]
print(myString)