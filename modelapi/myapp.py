import requests
import json
URL = "http://127.0.0.1:8000/stucreate/"

data = {
    'name':'Ashish',
    'roll':'202',
    'city':'Surat'
}

json_data = json.dumps(data)

r =requests.post(url=URL, data=json_data)
print(data)     