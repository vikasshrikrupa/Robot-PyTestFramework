import requests

payload={
        "name": "New1",
        "job": "API Testnew"
        }
resp=requests.put("https://reqres.in/api/users/2",data=payload)

print(resp.status_code)
print(resp.json())
assert (resp.json()['job'])=='API Testnew',"Job not matched."