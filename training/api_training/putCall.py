import requests

head = {
    'Accept':'text/plain'
}

# Submit a get request, and assign it to a variable:
response = requests.get("https://fakerestapi.azurewebsites.net/api/v1/Activities/12", headers=head)

print('Before Update')
print(response.json())

headerPut = {
    'Accept':'text/plain',
    'Content-Type': 'application/json'
}

putPayload = {
    "id": 15,
    "title": "Test Title 15",
    "dueDate": "2023-12-26T20:05:22.388Z",
    "completed": True
}

print('After Update')

responsePut = requests.put('https://fakerestapi.azurewebsites.net/api/v1/Activities/12',headers=headerPut,json=putPayload)

print(responsePut.json())