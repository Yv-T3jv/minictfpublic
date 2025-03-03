output = ""

with open("output.txt", "r") as f:
    output = f.read()

numlist = output.strip().split(" ")
for i in range(len(numlist)):
    numlist[i] = int(numlist[i])

flag = ""

for i in range(1, len(numlist) + 1):
    number = numlist[-i]
    flag = chr(number) + flag
    for i in range(len(numlist)):
        numlist[i] -= number

print(flag)

