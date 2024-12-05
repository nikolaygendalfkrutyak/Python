import re

def find_Rbr_s(str):
    pattern = r"^[R][b]+[r]"
    return re.findall(pattern, str)

print (find_Rbr_s("Rbbbbrs dRbbbrrr rbbbBr RbbbBr RbbbbR Rr Rbr RRbr" ))