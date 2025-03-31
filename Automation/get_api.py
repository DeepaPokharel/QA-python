import json
import requests

authorization= "token: QpwL5tke4Pnpja7X4"

url = "https://reqres.in/api/users"

def get_api():
    api = url
    headers= {"Authorization": authorization}
    response = requests.get(api, headers= headers)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent= 4)
    print("The user are:", json_str)
    print("-----------------------")

get_api()