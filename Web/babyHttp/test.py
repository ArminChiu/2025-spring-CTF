import requests, base64
s = requests.Session()
r = s.get("http://124.16.75.117:51001/index.php", stream=True)
p = base64.b64decode(r.headers['Password']).decode()[4:]
print(s.post(r.url, data={'Password': p}).text)