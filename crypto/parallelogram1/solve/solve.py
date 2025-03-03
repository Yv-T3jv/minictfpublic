from pwn import * 
p = connect("165.22.101.161", 9000)
p.sendline('1')
p.sendline('a'*4+'parallelogra'+'a'*16+'m')
p.recvuntil('?\n')
res = p.recvline()
res = bytes.fromhex(res[:-1].decode())
res = res[:16] + res[32:48]
p.sendline('2')
p.sendline(res.hex())
p.interactive()