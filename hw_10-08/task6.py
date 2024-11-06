import string


contactList = {}
while True:
    request = input("write add, delete, show or end: ")
    if request == "end":
        print ("Thanks for work")
        break
    elif request == "show":
        print (contactList)
    elif request == "delete":
        contact = input("Name of the contact to delete: ")
        if contact in contactList:
            del(contactList[contact])
            print(f"'{contact}' deleted")
        else:
            print ("There is no such contact. Use 'show' to check the list ")
    elif request=="add": 
        contact = input("Name of the contact to add: ")
        if ":" in contact:
            while " " in contact:
                contact=contact.replace(" ","")
            contact=contact.split(":")
            contactList[contact[0]]=contact[1]
            print(f"'{contact[0]}' added")
        else:
            if contact in contactList:
                print(f"This contact already exists with number {contactList[contact]}")
            else:
                secondString = input("That's a new contact. Do you know the number? ")
                if secondString!="no" :
                    while True: 
                        if secondString =="cancel":
                            print("Then try another option")
                            break
                        try: 
                            num = int(secondString)
                            contactList[contact]=num
                            print(f"'{contact}' added")
                            break
                        except:
                            print ("not a number")
                        secondString = input("Try the number again or 'cancel': ")
                else:
                    print("Than try another option")
    else:
        print("Wrong request")