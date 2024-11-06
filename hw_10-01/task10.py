x=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print (x)

# For not standart case
#x=[]
#while len(x)<4:
#    temp = list(map(int, input('Наступний массив ').split(",")))
#    x.append(temp)
#print(x)


cSum = 0
for i in x:
    cSum+=sum(i) 
print(cSum)