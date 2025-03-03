from Crypto.Util.number import getPrime, bytes_to_long
#Can you decrypt RSA?
flag = b'IRS{REDACTED}'
p = getPrime(1024)
q = getPrime(1024)
N = p * q 
phi = (p - 1) * (q - 1)
e = 65537
m = bytes_to_long(flag)
c = pow(m, e, N)
print(f"{N = }")
print(f"{phi = }")
print(f"{e = }")
print(f"{c = }")