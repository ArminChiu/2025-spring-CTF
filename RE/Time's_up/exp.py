from pwn import *

# 设置连接
conn = remote('124.16.75.117', 51004)
conn.recvuntil(b'Challenge: ')

# 接收挑战、计算并发送结果
challenge = conn.recvline().strip()
result = eval(challenge.decode())
conn.sendline(str(result).encode())

# 进入交互模式
conn.interactive()