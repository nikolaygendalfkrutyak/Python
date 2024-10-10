translations = {}
while True:
    myString = input("write word, end or show: ")
    if myString == "end":
        print ("Thanks for work")
        break
    elif myString == "show":
        print (translations)
    else: 
        if ":" in myString:
            while " " in myString:
                myString=myString.replace(" ","")
            myString=myString.split(":")
            translations[myString[0]]=myString[1]
        else:
            if myString in translations:
                print(translations[myString])
            else:
                secondString = input("That's a new word for dict \n Do you know the translation? ")
                if secondString!="no":
                    translations[myString]=secondString
                else:
                    print("Try another word")
    