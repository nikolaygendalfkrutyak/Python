import re

def find_bank_nummer(str):
    pattern = r"^([0-9]{4}[- ]?){4}"
    return re.match(pattern, str)

print (find_bank_nummer("88888888-8888 8888"))