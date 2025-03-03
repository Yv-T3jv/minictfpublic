import hashlib
from ecdsa.curves import NIST256p
from ecdsa.ellipticcurve import Point
from random import SystemRandom
from Crypto.Util.number import bytes_to_long
rand = SystemRandom()

flag = b'IRS{REDACTED}'

curve = NIST256p.curve 
G = NIST256p.generator
n = NIST256p.order

d = bytes_to_long(flag)
assert(d < n - 1)
Q = d * G 

print(f"Public key (Q): ({Q.x()}, {Q.y()})")

m1 = b'Have you heard of ECDSA before?'
m2 = b'Are you a parallelogram?'

def sign(message, id, k):
    if k == -1:
        k = rand.randint(1, 2 ** 100)
    
    h = int(hashlib.sha256(message).hexdigest(), 16)
    R = k * G
    r = R.x() % n 
    
    k_inv = pow(k, -1, n)
    s = (k_inv * (h + d * r)) % n
    print(f"Signature of {message}:")
    print(f"r{id} = {r}")
    print(f"s{id} = {s}")

sign(m1, 1, -1)
sign(m2, 2, -1)