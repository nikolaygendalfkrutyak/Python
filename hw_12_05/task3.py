import re

def match_email(str):
    pattern = r"^[A-Za-z0-9\-_]*[@][A-Za-z]*[.][A-Za-z]*$"
    return re.match(pattern, str)

print (match_email("abraham-@mail.com"))
print (match_email("abraham-_@mail.com"))

print (match_email("abraham--@mail.com"))