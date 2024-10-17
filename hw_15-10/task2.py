import random
def create_easy_crackable_password(length, is_extra):
    password = ""
    if is_extra:
        for i in range (length):
            a=random.randint(33,126)
            password+=chr(a)
        
    else:
        for i in range (length):
            a=0
            while True:
                a=random.randint(48, 123)
                if 49<=a<=57 or 65<=a<=90 or 97<=a<=122:
                    break
            password+=chr(a)
    
    return(password)
    
print(create_easy_crackable_password(8, False))