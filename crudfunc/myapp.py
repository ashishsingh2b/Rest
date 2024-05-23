import requests
import json

URL = 'http://127.0.0.1:8000/studentapi/'

def get_data(id=None):
    data = {}
    if id  is not None:
        data = {'id':id}
    json_data=json.dumps(data)
    headers = {'content-Type':'application/json'}
    r = requests.get(url=URL,headers=headers,data=json_data)
    data =r.json()
    print(data)
#get_data()
    
def post_data():
 data = {
        'name':'Ramji',
        'roll':145,
        'city' : 'Ayodhya',
    }


 json_data = json.dumps(data)
 headers = {'content-Type':'application/json'}
 r = requests.post(url=URL,headers=headers,data=json_data)
 data =r.json()
 print(data)

#post_data()

def update_data():
    data = {
      'id':1,
      'name':'Bittu',
      'roll':10,
      'city':'Surat City',
    }

    json_data = json.dumps(data)
    headers = {'content-Type':'application/json'}
    r = requests.put(url = URL ,headers=headers, data = json_data)
    print(r.json())
#update_data()

def delete_data():
    data ={'id':3}

    json_data = json.dumps(data)
    headers = {'content-Type':'application/json'}
    r = requests.delete(url = URL ,headers=headers, data = json_data)
    print(r.json())
delete_data()
 


