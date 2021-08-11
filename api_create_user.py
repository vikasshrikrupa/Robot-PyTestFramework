import requests

payload={
        "name": "New1",
        "job": "Test"
        }
resp=requests.post("https://reqres.in/api/users",data=payload)

print(resp.status_code)
print(resp.json())
assert resp.json()['job']=='Test', "Job not matching."