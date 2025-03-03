#See https://codeforces.com/blog/entry/82924
from os import urandom 
from Crypto.Util.number import bytes_to_long
import time
from pwn import * 
p = process("python3 server.py", shell=True)
def ask(lst):
    newlst = [str(x) for x in lst]
    p.sendline(' '.join(newlst))
    p.recvline()
    return int(p.recvline())
def gen(n):
    if n == 0:
        return [1, [1]]
    else:
        x, prev = gen(n-1)
        new = []
        for i in range(1, 2**(n-1)):
            add = []

            for k in prev[i-1]:
                add.append(k)
                add.append(k+x)
            add.append(2*x+i)
            new.append(add)
            add = []
            for k in range(1, x+1):
                if k in prev[i-1]:
                    add.append(k)
                else:
                    add.append(x + k)
            new.append(add)
        res = []
        for i in range(x+1, 2*x+1):
            res.append(i)
        new.append(res)
        res = []
        for i in range(1, 2*x+2**(n-1)):
            res.append(i)
        new.append(res)
        return (2*x + 2**(n-1) -1, new)
def recover(n, results):
    assert(len(results) == 2 ** n)
    if n == 0:
        return results
    m = results[-2]
    back = []
    for i in range(2**(n-1)-1):
        a = results[2 * i]
        b = results[2 * i + 1]
        back.append((a+b+m)%2)
    backsum = sum(back)
    secsum = results[-2]
    firsum = results[-1] - backsum - secsum 
    fir = []
    sec = []
    for i in range(2**(n-1)-1):
        a = results[2 * i]
        b = results[2 * i + 1]
        fir.append((a+b-m)//2)
        sec.append((a-b+m)//2)
    fir.append(firsum)
    sec.append(secsum)
    return recover(n-1, fir) + recover(n-1, sec) + back 
k = 5
n, qry = gen(k)
res = []
for i in range(2**k):
    res.append(ask(qry[i]))
x = recover(k, res)
x = [str(k) for k in x]
p.sendline(" ".join(x))
p.interactive()