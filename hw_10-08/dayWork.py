# import string
# text=input("input: ").split(" ")
# res_dict = {}
# for i in text:
#     if i in res_dict:
#         res_dict[i]+=1
#     else:
#         res_dict[i]=1
# print(res_dict)

data = [
    '1 Bob Simson 19.58$ decorations',
    '2 Mary 66.7$ food',
    '3 Mary 98.91$ toys',
    '4 Aleksa 72.29$ drinks',
    '5 Maria Simson 84.48$ food',
    '6 Aleksa 100.41$ accessories',
    '7 Mary 19.9$ accessories',
    '8 Bob Simson 83.88$ drinks',
    '9 Bob Simson 58.21$ instruments',
    '10 Maria Simson 20.61$ accessories',
]
res={}
for i in data:
    tempList = i.split(" ")
    if tempList[-1] in res:
        res[tempList[-1]]+=float(tempList[-2][:-1])
    else:
        res[tempList[-1]]=float(tempList[-2][:-1])
    
print(res)