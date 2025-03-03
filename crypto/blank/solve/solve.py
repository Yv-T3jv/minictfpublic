with open("enc.txt", "r") as f:
    x = f.read()
x = x.split('\n')[:-1]
for k in x:
    res = ""
    for i in k:
        if i == ' ': res += "0"
        else: res += "1"
    print(chr(int(res, 2)), end = '')