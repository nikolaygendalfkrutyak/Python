# def count_money(myMoney, is_final=True):
#     zero_nine= ["", "one", "two", "three", "four", "five","six","seven","eight","nine"]
#     tens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", 
#             "nineteen"]
#     twenty_ninty=["", "", "twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety"]
#     try:
#         myMoney=float(myMoney)
#         answer = ""
#         cents= int((myMoney-int(myMoney))*100)
#         myMoney=int(myMoney)
#         thousands = myMoney //1000
#         if thousands:
#             answer += f"{count_money(thousands,False)} thousand "
            
#         myMoney%=1000
#         hundreds = myMoney //100
#         if hundreds:
#             answer+=f"{zero_nine[hundreds]} hundred "
#         myMoney%=100
#         ten = myMoney //10
#         myMoney%=10
#         if ten:
#             if ten!=1:            
#                 answer+=f"{twenty_ninty[ten]} {zero_nine[myMoney]} "
#             else:
#                 answer+=f"{tens[myMoney]}"
#         else:
#             answer+=f"{zero_nine[myMoney]}"
#         if not myMoney and not answer:
#             answer="Zero"
#         if (is_final):
#             answer+=" dollar"
#             if myMoney!=1 or ten==1:
#                 answer+="s"
#             if cents:
#                 answer+=f" and {count_money(cents, False)} cent"
#                 if cents != 1:
#                     answer+="s"
#         else:
#             answer.lower()
#         return (answer)
        
#     except:
#         return("Wrong format")
    

# myMoney = input("Money: ")
# print(count_money(myMoney))
salary = {
    'January': 1000,
    'February': 1500,
    'March': 2000,
    'April': 2500,
    'May': 3000,
    'June': 3500,
    'July': 4000,
    'August': 4500,
    'September': 5000,
    'October': 5500,
    'November': 6000,
    'December': 6500
}
file = open('data.txt', 'w')
for i in range(len(salary)):
    file.write(f"{salary.keys[i]} : {salary.values[i]}$\n")
file.close()