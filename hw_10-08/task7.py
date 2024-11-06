exchange= {
    "$":"0.9E",
    "E":"47h",
    "h":"0.021$"
}
money = input("Money: ").split(" ")
amount=float(money[0][:-1])
curency = money[0][-1]
curencyNeeded=money[2]
while curency!=curencyNeeded:
    amount*=float(exchange[curency][:-1])
    curency=exchange[curency][-1]
print(f"{amount}{curency}")
