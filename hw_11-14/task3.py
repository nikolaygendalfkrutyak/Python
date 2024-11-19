def functional(func):
    def inner(my_list):
        return sum(list(func(my_list)))
    return inner

def plus_five(my_list):
    for i in range(len(my_list)):
        yield my_list[i]+5
x = functional(plus_five)            
print (x([1, 2, 3, 4, 5]))
