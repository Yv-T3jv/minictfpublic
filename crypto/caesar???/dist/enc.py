from random import randint 
secret_msg = '''
此消息的内容是保密的
'''
chinese_ascii_start = 13312
chinese_ascii_end = 40959
num_char = chinese_ascii_end - chinese_ascii_start + 1
def to_int(c):
  idx = ord(c) - chinese_ascii_start
  return idx 
def to_chinese(idx):
  return chr(idx + chinese_ascii_start)
def enc_message(msg, offset):
  res = ""
  for c in msg:
    if ord(c) >= chinese_ascii_start and ord(c) <= chinese_ascii_end:
      idx = to_int(c)
      newidx = (idx + offset) % num_char 
      newchar = to_chinese(newidx)
      res += newchar
    else:
      res += c
  return res 
enc = enc_message(secret_msg, randint(0, num_char - 1))
print(f"Chinese Caesar Cipher? Here's my encrypted message: {enc}") 