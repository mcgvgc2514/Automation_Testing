import requests

header = {
    "Accept" :'text/plain',
    'Content-Type': 'application/json'
}

request_payload = {
    "id": 155,
    "title": "presanth api testing course 3",
    "dueDate": "2023-12-21T14:59:03.826Z",
    "completed": True
} 

response = requests.post("https://fakerestapi.azurewebsites.net/api/v1/Activities", 
                            headers=header, 
                            json=request_payload)

print(response.status_code)
print(response.json())
data = response.json()

assert response.status_code == 200
assert data['id'] == 155

# Post request creates a new line
# Put request updates a previously existing line