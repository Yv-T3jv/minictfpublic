from Crypto.Util.number import getPrime, bytes_to_long
import random 
primes = [getPrime(1024) for _ in range(20)]
def enc(N, m):
    e = 65537
    c = pow(m, e, N)
    return (N, e, c)
flag = b'IRS{REDACTED}'
m = bytes_to_long(flag)
encs = []
for i in range(10):
    p = random.choice(primes)
    q = random.choice(primes)
    encs.append(enc(p * q, m))
print(encs)