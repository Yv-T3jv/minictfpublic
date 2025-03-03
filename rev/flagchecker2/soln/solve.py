number = 5998755151006221569035854804378700021992824594991737161
flag = ""

while number != 0:
    flag += chr(number % 128)
    number //= 128

print(flag)