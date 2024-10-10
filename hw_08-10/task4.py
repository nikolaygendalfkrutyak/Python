myWords = input("Text: ")
allWords = myWords.split(" ")
myDict = {}
for i in allWords:
    if i in myDict:
        myDict[i]+=1
    else:
        myDict[i]=1
print (myDict)