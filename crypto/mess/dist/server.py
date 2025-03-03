from Crypto.Util.number import *
from Crypto.Random.random import getrandbits
p, q = [int(x) for x in open("keys").read().split()]
#p, q are 1024 bit primes generated with getPrime(1024)
print("RSA, LCG and Zero Knowledge Proofs")
print("Good luck!")

#RSA
N = p * q
phi = (p - 1) * (q - 1)
e1 = 1234567891011121314156942049111111
d1 = pow(e1, -1, phi)
print(f"{N = }")
print(f"{e1 = }")
print(f"{d1 = }") #Whoops! 
e2 = getrandbits(2048)
print(f"{e2 = }")
flag = b'IRS{REDACTED}'
m = bytes_to_long(flag)
c2 = pow(m, e2, N)

#LCG
start = getrandbits(2000)
a = getrandbits(2000)
c = getrandbits(2000)
def kthLCG(k):
    cur = (a, c)
    res = start 
    while k > 0:
        if (k % 2 == 1): res = (res * cur[0]) + cur[1]
        res %= N
        cur = (cur[0] * cur[0], cur[0] * cur[1] + cur[1])
        cur = (cur[0] % N, cur[1] % N)
        k //= 2
    return res 

#Zero Knowledge Proofs
r = 32317006071311007300338913926423828248817941241140239112842009751400741706634354222619689417363569347117901737909704191754605873209195028853758986185622153212175412514901774520270235796078236248884246189477587641105928646099411723245426622522193230540919037680524235519125679715870117001058055877651038861847280257976054903569732561526167081339361799541336476559160368317896729073178384589680639671900977202194168647225871031411336429319536193471636533209717077448227988588565369208645296636077250268955505928362751121174096972998068410554359584866583291642136218231078990999448652468262416972035911852507045361090559
g = 2
print("I know the encrypted flag")
print("I'll prove it to you!")
print(f"y = {pow(g, c2, r)}")
cur = 0
for _ in range(2):
    idx = int(input("Give me a number to feed into my super secure LCG: "))
    cur += idx 
    rng = kthLCG(cur)
    C = pow(g, rng, r)
    print(f"{C} = ")
    print("Do you want rng (1) or c2 + rng (2)?")
    opt = int(input())
    if opt == 1:
        print(f"{rng = }")
    elif opt == 2:
        print(f"{c2 + rng = }")
print("Goodbye!")