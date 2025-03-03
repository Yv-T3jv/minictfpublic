with open(r"C:\Users\rain\Documents\UNAFFILATED-MINICTF-2024\solves\forens\conceal + purify skill 3 is a bit broken\not-quite-fading-into-the-moonlight.so", 'rb') as elf:
    contents = elf.read()

contents = contents[4:] # remove magic number
bits = []

for byte in contents:
    msb = byte >> 7
    bits.append(msb)

try: # crude way to prevent IndexError caused by out-of range (number of "useful bytes" is not divisible by 8)
    for i in range(0, len(bits), 8): #prints flag
        eight_bits = ''.join(str(bits[j]) for j in range(i, i+8))
        byte = int(eight_bits, base = 2)
        if byte != 0x08: print(chr(byte), end="") # prevent backspaces from being printed
except Exception as e:
    print(e)