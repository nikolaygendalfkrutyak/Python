def total_for_each(arr, cat):
    """ Helps to find sum of money values for some categories

    Args:
        arr (Array): array of arrays of data. 
            Each contains 3 positions [name_of_customer (String), category_of_shopping(String), money_spent(float)]  
        cat (String): "name" or "category" 
            Helps to understand by which of 2 categories (name_of_customer or category_of_shopping) should we divide our data

    Returns:
        dict : returns pairs (category_name : total_money_spent) 
    """
    if cat=="name":
        my_index =0
    elif cat=="category":
        my_index=1
    else:
        return (total(arr))
    res={}
    for i in arr:
        if i[my_index] in res:
            res[i[my_index]] = round((res[i[my_index]]+i[2]), 2)
        else:
            res[i[my_index]]=i[2]
    return res
def total(arr):
    """Sums all money spent aside of names and categories

    Args:
        arr (Array of Arrays): in each array there is 3 parameters, the last of them is money amount which we need
    """
    mySum=0
    for i in arr:
        mySum=round(mySum+i[-1], 2)
    return(mySum)
def parse_doc(link):
    """parse data from a file with given path to a needed format

    Args:
        link (String): link to the file where data is stored

    Returns:
        array: returns sorted data after changning type if needed
    """
    try:
        file = open(link, 'r')
        res = []
        for i in file.readlines():
            i=i.split(" ")
            name = " ".join(i[1:-2])
            category =i[-1][:-1]
            money = round(float(i[-2][:-1]), 2)
            res.append([name, category, money])
        file.close()
        return res
    except:
        return None
data = parse_doc("hw_10_test.txt")    
print(f"Total sum is: {total(data)}")
print(f"Each member spent: {total_for_each(data, "name")}")
print(f"For each category were spent: {total_for_each(data, "category")}")
print(int(100*(3.889)))