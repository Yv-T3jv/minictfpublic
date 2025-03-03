from os import urandom 
from Crypto.Util.number import bytes_to_long
N = 81
arr = bytes_to_long(urandom((N+8)//8)) % (2 ** N)
arr = bin((arr))[2:].zfill(N)
arr = [int(i) for i in arr]
Qlimit = 32 
FLAG = b'IRS{REDACTED}'
for i in range(Qlimit):
    print(f"Select a subset of integers, S from 1 to {N}, and I will return the sum of arr[i] for i in S.")
    try:
        inp = input().split()
        inp = [int(x) for x in inp]
        if len(list(set(inp))) != len(inp):
            print("All values should be distinct")
            break
        res = [arr[x-1] for x in inp]
        res = sum(res)
        print(res)
    except:
        print("An error occurred")
        break

print("Now guess my binary array!")
try:
    guess = input().split()
    guess = [int(x) for x in guess]
    if guess == arr:
        print("You win!")
        print(FLAG)
except:
    print("An error occurred.")
