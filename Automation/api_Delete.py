import requests
import json

url = "https://reqres.in/"
authorization = "token any_token"

# def delete_request():
#     api = url + "api/users/2"
#     headers= {"Authorization": authorization}
#     response = requests.delete(api, headers= headers)
#     assert response.status_code == 204
#     print("the user details is deleted")

def delete_request(user_id):
    api = url + "api/users/{user_id}"
    headers= {"Authorization": authorization}
    response = requests.delete(api, headers= headers)
    assert response.status_code == 204
    print("the deleted user id is:",user_id)
    print("--------------------")
    print("the user details is deleted")

delete_request(2)
