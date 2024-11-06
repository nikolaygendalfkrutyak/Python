l = int(input("lentgth = "))
for i in range (l):
    myStr = ""
    if 2*i<l:
        myStr+=i*" "+(l-2*i)*"*"+i*" "
    else:
        myStr+=(l-i-1)*" "+(2*i-l+2)*"*"+(l-i-1)*" "
    print(myStr)
