# import random
# calendar = ["січень", "лютий", "березень", "квітень", "травень", "червень", "липень", "серпень",
#             "вересень", "жовтень", "листопад", "грудень"]
# x=[random.randint(1000,10000) for _ in range(12)]
# print(x)
# print(f"найменша зарплата була у місяці -  {calendar[x.index(min(x))]}")

# badString=input("введіть свої дані: ")
# while "  " in badString:
#     badString=badString.replace("  ", " ")
# print (badString)

#print(len(input("введіть свої дані: ").split(" ")))

import string
badString=input("введіть свої дані: ")
for i in string.punctuation:
    while i in badString:
        badString=badString.replace(i, "")

print (' '.join(badString.split(" ")))