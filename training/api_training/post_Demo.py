# Uses this tutorial: https://www.youtube.com/watch?v=eAm6RGROLY0

import requests
import json

base_url = 'https://reqres.in/api/users'

headers_test = {'Content-Type' : 'application/json'}

json_file = open('training/api_training/users.json')
json_payload = json.load(json_file)

response = requests.post(url=base_url, headers=headers_test, json=json_payload)
print(response.status_code)
print(response.text)

