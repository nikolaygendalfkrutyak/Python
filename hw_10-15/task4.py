import math


def next_number(arr):
    ar = is_arithmetik_progression(arr)
    ge = is_geometrik_progression(arr)
    ex = is_exp_progression(arr)
    if ar[0]:
        return ar[1]
    elif ge[0]:
        return ge[1]
    elif ex[0]:
        return ex[1]
    else:
        return -1
def is_arithmetik_progression(arr):
    diff = arr[1]-arr[0]
    for i in range(2, len(arr)):
        if arr[i]!=arr[0]+diff*(i):
            return (False, -1)
    return (True, arr[-1]+diff)
def is_geometrik_progression(arr):
    diff = arr[1]/arr[0]
    for i in range(2, len(arr)):
        if arr[i]!=arr[0]* (diff**(i)):
            return (False, -1)
    return (True, arr[-1]*diff)
def is_exp_progression(arr):
    grade = math.log(arr[1], 2)
    arr1=[]
    for i in arr:
        arr1.append(i**(1/grade))
    ar = is_arithmetik_progression(arr1)
    return (ar[0], ar[1]**grade)

print(next_number([1, 4, 9, 16, 25]))