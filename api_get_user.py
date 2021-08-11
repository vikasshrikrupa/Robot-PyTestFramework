import requests

p='page2'
res=requests.get("https://reqres.in/api/users?",params=p)
assert res.status_code==200, "Code dose not match."
print(res.json())
print(res.headers)
print(res.encoding)
print(res.url)
json_res=res.json()
print(json_res['total'])
print(json_res['total_pages'])
assert (json_res['total_pages'])==2, "No pages not matching."
print(json_res['data'][0]['email'])
assert (json_res['data'][0]['email']).endswith('reqres.in'),"Email not matching."
print(json_res['data'][1]["last_name"])
print(json_res['support']['url'])