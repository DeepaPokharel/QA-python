import requests
import json

url = "https://reqres.in/"
authorization = "token any_token"

def put_update(user_id):
# def put_update():
    api = url + "api/users/{user_id}"
    # api = url + "api/users/2"
    headers= {"Authorization": authorization}
    data = {
        "name": "morpheus",
        "job": "zion resident"
    }
    response = requests.put(api, json= data, headers= headers)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent= 4)
    print("the updated user is:", json_str)

# put_update()
put_update(5)