from pwn import *
import os

os.environ["GDB"] = "/usr/local/bin/pwndbg"
context.terminal = ["tmux", "splitw", "-h"]
context.binary = "./execver"

# 启动进程
p = process("./execver")

# 附加 GDB
gdb.attach(p, gdbscript="""
    break *main
    continue
""")

# 交互
p.interactive()