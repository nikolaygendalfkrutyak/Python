'''It was wrong but no one needs it from me...'''

def category(arr):
    money, categories=help_func(arr)
    res={}
    for i in categories:
        if i in res:
            res[i]+=0
        else:
            res[arr[1]]=arr[0]
    return res
def total(arr):
    return(sum (help_func(arr)[0], key=[0]))
def help_func(arr):
    money=[]
    categories=[]
    for i in arr:
        money.append(float(i.split(" ")[-2][:-1]))
        categories.append(i.split(" ")[-1])
    return(money, categories)
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

    
print(total(data))
print(category(data))