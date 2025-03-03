from pwn import *
from functools import reduce
from Crypto.Util.number import long_to_bytes
import sys 
sys.setrecursionlimit(10000)

enc = []
for i in range(3):
    p = connect("165.22.101.161", 9002)
    p.recvline()
    p.recvline()
    for _ in range(4): 
        exec(p.recvline())    
    fakephi = e1 * d1 - 1
    p.sendline(str(0))
    p.sendline("1")
    p.sendline(str(fakephi))
    p.sendline("2")
    for _ in range(5):
        p.recvline()
    exec(p.recvline())
    for _ in range(2): p.recvline()
    exec(p.recvline().replace(b"c2 + rng", b"lol"))
    c = lol - rng 
    print(f"{N = }")
    enc.append((e2, c))
def red(p1, p2):
    if p1[0] > p2[0]:
        p1, p2 = p2, p1
    if p1[0] == p2[0]: return p1 
    if p1[0] == 0: return p2 
    r = p2[0] % p1[0]
    q = p2[0] // p1[0]
    return red(p1, (r, (p2[1] * pow(p1[1], -q, N)) % N))
res = reduce(red, enc)
print(long_to_bytes(res[1]))