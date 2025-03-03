import random

CHARSET = "J2PDgn3ACBfdW7mkwS6e0ZaYq9GjEULFzxpXb85ycNvTt_4r1}KuQOVolhIHsR{M"

with open("out.txt", "r") as file:
    flag = file.read()

random.seed("IRS{sa")

resultpool = []
flagformat = "IRS{"
flaghead = "IRS{"

for c1 in CHARSET:
    for c2 in CHARSET:
        layers = []
        
        seed = flagformat + c1 + c2
        flaghead = seed
        random.seed(seed)
        result = flag

        for i in range(100):
            layer = "".join([CHARSET[random.randint(0, len(CHARSET)-1)] for j in range(len(flag))])
            flaghead = "".join([CHARSET[CHARSET.index(flaghead[j]) ^ CHARSET.index(layer[j])] for j in range(len(flaghead))])
            random.seed(flaghead)
            layers.append(layer)

        for layer in layers:
            result = "".join([CHARSET[CHARSET.index(result[j]) ^ CHARSET.index(layer[j])] for j in range(len(result))])

        print(f"{seed} {result}")
        if result[:4] == "IRS{":
            resultpool.append(result)

print(resultpool)