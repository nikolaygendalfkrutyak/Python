arr = [
    ("cola","drink", "1.5 E"),
    ("pepsi","drink", "1.4 E"),
    ("orange juice","drink", "2 E"),
    ("carbonara", "pasta", "15 E"),
    ("bolonjese", "pasta", "13 E"),
    ("hot dog", "snack", "3 E"),
    ("hamburger","snack", "2.5 E"),
    ("risotto","risotto", "15 E")    
]
ans={}
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if set(arr[i]) & set(arr[j]):
                name = str(set(arr[i])&set(arr[j]))[2:-2]
                if name in ans:
                    ans[name]=ans[name] | set([arr[i][0], arr[j][0]])
                else:
                    ans[name]=set([arr[i][0], arr[j][0]])

print (ans)

