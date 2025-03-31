# import libraries
import requests
import json

url = "https://reqres.in/"

authorization = "token any_token"

def post_request():
    api = url + "api/users"
    headers= {"Authorization": authorization}
    data= {
        "name": "Hari",
        "job": "QA tester",
        "number": 9823451980
    }
    response = requests.post(api, json= data, headers= headers)
    assert response.status_code == 201
    json_data = response.json()
    user_id = json_data["id"]
    json_str = json.dumps(json_data, indent= 4)
    print("the new user id is:", user_id)
    print("-------------------")
    print("the created user is:", json_str)

def post_login():
    api1 = url + "api/login"
    headers= {"Authorization": authorization}
    data = {
        "email": "eve.holt@reqres.in",
        "password": "city123@"
    }
    response = requests.post(api1, json= data, headers= headers)
    assert response.status_code == 200
    json_data = response.json()
    user_id = json_data["token"]
    print("the new user token is:", user_id)

post_login()
