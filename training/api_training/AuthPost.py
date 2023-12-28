import requests

head = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer dde9023f56ff7dbde8ac8b29afeb0f8f6bc768d7791f6617d23e90e25dbe2648'
}

body = {
    "name":"Prasanth",
    "email":"test_jha32dsaf42345wes@bernier.test",
    "gender":"male",
    "status":"active"
} 

url = 'https://gorest.co.in/public/v2/users'

response = requests.post(url, headers=head, json=body)

print(response.json())
assert response.status_code == 201

getResponse = requests.get(url + '/' + str(response.json()['id']), headers=head)

print(getResponse.json())
