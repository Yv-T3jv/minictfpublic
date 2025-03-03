import random

CHARSET = "J2PDgn3ACBfdW7mkwS6e0ZaYq9GjEULFzxpXb85ycNvTt_4r1}KuQOVolhIHsR{M"
flag = "IRS{REDACTED}"

for i in range(100):
    random.seed(flag[:6])
    salt = "".join([CHARSET[random.randint(0, len(CHARSET)-1)] for j in range(len(flag))])
    flag = "".join([CHARSET[CHARSET.index(flag[j]) ^ CHARSET.index(salt[j])] for j in range(len(flag))])

with open("out.txt", "w") as file:
    file.write(flag)

