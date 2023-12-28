import requests

head = {
    'Accept':'text/plain'
}

# Submit a get request, and assign it to a variable:
response = requests.get("https://fakerestapi.azurewebsites.net/api/v1/Activities/3", headers=head)

print(response.status_code)
print(response.json())

assert response.status_code == 200
