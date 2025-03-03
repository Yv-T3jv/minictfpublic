FLAG = "IRS{sample}"

out = [0] * len(FLAG)

for i in range(len(FLAG)):
    value = ord(FLAG[i])
    for j in range(i + 1):
        out[j] += value

with open("output.txt", "w") as f:
    for num in out:
        f.write(str(num) + " ")