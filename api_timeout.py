import requests

resp=requests.get("https://httpbin.org/delay/5",timeout=8)
print(resp.status_code)