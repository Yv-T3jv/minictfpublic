from Crypto.Util.number import getPrime, bytes_to_long
from random import randint
p = getPrime(1024)
q = getPrime(1024)
N = p * q * q * p
phi = p * q * (p - 1) * (q - 1) 
d = getPrime(2000) #hm... 
e = pow(d, -1, phi)
flag = b'IRS{REDACTED}'
m = bytes_to_long(flag)
c = pow(m, e, N)
print(f"{N = }")
print(f"{e = }")
print(f"{c = }")