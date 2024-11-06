l, h = int(input("lentgth = ")), int(input("height = "))
for i in range (h):
    myStr = ""
    for j in range (l):
        if i and i!=h-1 and j and j!=l-1:
           myStr+=" "
        else:
            myStr+="*"
    print(myStr)