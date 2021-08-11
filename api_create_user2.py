import requests
import json

mydata=open("data.json","r").read()
resp=requests.post("https://reqres.in/api/users",data=json.loads(mydata))
print(resp.json())
assert resp.json()['job']=='Auto_Tester', "Job not matching."