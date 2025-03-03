import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
#What is AES?
#What is ECB mode in a block cipher? 
#https://docs.google.com/presentation/d/1aHQbaXmbYwVOJO49_aqPKlbYajb8ukbnZOVTgB01g0I/edit
KEY = os.urandom(16)
FLAG = b'IRS{REDACTED}'

while True:
    print("Welcome! Pick one of the two operations:\n1. Encode any string, well... basically any string\n2. Get flag")
    opt = input()
    try:
        opt = int(opt)
    except:
        print("Invalid Option")
        break 
    if opt == 1:
        print("What would you like to encrypt?")
        inp = input() 
        if inp.find("parallelogram") == -1:
            inp = inp.encode()
            inp = pad(inp, 16)
            cipher = AES.new(KEY, AES.MODE_ECB) #ECB is so simple... why would anyone use CBC
            enc = cipher.encrypt(inp)
            print(enc.hex())
        else:
            print("Hey! You aren't allowed to use that word!")
    elif opt == 2:
        print("Try to get the flag... But you won't")
        print("The decrypted output has to contain parallelogram as a substring")
        print("Give me the encrypted result, in hex")
        inp = input() 
        try:
            inp = bytes.fromhex(inp)
            cipher = AES.new(KEY, AES.MODE_ECB)
            plaintext = cipher.decrypt(inp)
        except Exception as e:
            print(e)  
            print("Invalid input")
        print(plaintext)
        if plaintext.find(b"parallelogram") != -1:
            print("You are a parallelogram!")
            print(FLAG)
        else:
            print("You are not a parallelogram :(")
        break
    else:
        print("Invalid Option")
        break 
