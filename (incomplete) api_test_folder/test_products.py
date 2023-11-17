import requests
import pytest
import json

# Load in API calls:
with open('api_response.json') as user_file:
    api_response = json.load(user_file)
    
def test_api_id_values():
    # First we test the "id" values in the api calls, using positive and negative testing:
    assert (api_response['products'][0]["id"]) == 1
    assert (api_response['products'][0]["id"]) != "1"
    assert (api_response['products'][0]["id"]) != -37
    assert (api_response['products'][0]["id"]) != 124
    assert (api_response['products'][0]["id"]) != False
    assert (api_response['products'][1]["id"]) == 2
    assert (api_response['products'][1]["id"]) != "2"
    assert (api_response['products'][1]["id"]) != -9
    assert (api_response['products'][1]["id"]) != 1222
    assert (api_response['products'][1]["id"]) != False
    assert (api_response['products'][1]["id"]) != True
    assert (api_response['products'][2]["id"]) == 3
    assert (api_response['products'][2]["id"]) != "3"
    assert (api_response['products'][2]["id"]) != 0
    assert (api_response['products'][2]["id"]) != 942
    assert (api_response['products'][2]["id"]) != False
    assert (api_response['products'][2]["id"]) != True

def test_api_name_values():
    # Next we test the "id" values in the api calls, using positive and negative testing:
    assert (api_response['products'][0]["name"]) == "Product A"
    assert (api_response['products'][0]["name"]) != "Product C"
    assert (api_response['products'][0]["name"]) != 3333
    assert (api_response['products'][2]["name"]) != False
    assert (api_response['products'][2]["name"]) != True
    assert (api_response['products'][1]["name"]) == "Product B"
    assert (api_response['products'][1]["name"]) != "Product 24"
    assert (api_response['products'][1]["name"]) != 452
    assert (api_response['products'][2]["name"]) != False
    assert (api_response['products'][2]["name"]) != True
    assert (api_response['products'][2]["name"]) == "Product C"
    assert (api_response['products'][2]["name"]) != "Prodcut A"
    assert (api_response['products'][2]["name"]) != -52
    assert (api_response['products'][2]["name"]) != False
    assert (api_response['products'][2]["name"]) != True

def test_api_category_values():
    # Next we test the "catagory" values in the api calls, using positive and negative testing:
    assert (api_response['products'][0]["category"]) == "Electronics"
    assert (api_response['products'][0]["category"]) != "j4pqiofj ;aeirw "
    assert (api_response['products'][0]["category"]) != (3-4-6*28)
    assert (api_response['products'][0]["category"]) != False
    assert (api_response['products'][0]["category"]) != True
    assert (api_response['products'][1]["category"]) == "Books"
    assert (api_response['products'][1]["category"]) != "Televisions"
    assert (api_response['products'][1]["category"]) != 9999999^444444
    assert (api_response['products'][1]["category"]) != False
    assert (api_response['products'][1]["category"]) != True
    assert (api_response['products'][2]["category"]) == "Electronics"
    assert (api_response['products'][2]["category"]) != "Books"
    assert (api_response['products'][2]["category"]) != -0
    assert (api_response['products'][2]["category"]) != False
    assert (api_response['products'][2]["category"]) != True

def test_api_price_values():
    # Next we test the "price" values in the api calls, using positive and negative testing:
    assert (api_response['products'][0]["price"]) == 99.99
    assert (api_response['products'][0]["price"]) != "99.99"
    assert (api_response['products'][0]["price"]) != 849327.1838395
    assert (api_response['products'][0]["price"]) != -849327.1838395
    assert (api_response['products'][0]["price"]) != False
    assert (api_response['products'][0]["price"]) != True
    assert (api_response['products'][1]["price"]) == 14.99
    assert (api_response['products'][1]["price"]) != "14.99"
    assert (api_response['products'][1]["price"]) != 20.88
    assert (api_response['products'][1]["price"]) != 0
    assert (api_response['products'][1]["price"]) != False
    assert (api_response['products'][1]["price"]) != True
    assert (api_response['products'][2]["price"]) == 199.99
    assert (api_response['products'][2]["price"]) != "199.99"
    assert (api_response['products'][2]["price"]) != 200.01
    assert (api_response['products'][2]["price"]) != 199
    assert (api_response['products'][2]["price"]) != False
    assert (api_response['products'][2]["price"]) != True

def test_api_price_values():
    # Next we test the "price" values in the api calls, using positive and negative testing:
    assert (api_response['products'][0]["in_stock"]) == True
    assert (api_response['products'][0]["in_stock"]) != "True"
    assert (api_response['products'][0]["in_stock"]) != 8427.1838395
    assert (api_response['products'][0]["in_stock"]) != -84933.1838395
    assert (api_response['products'][0]["in_stock"]) != False
    assert (api_response['products'][1]["in_stock"]) == False
    assert (api_response['products'][1]["in_stock"]) != "False"
    assert (api_response['products'][1]["in_stock"]) != 20.784
    assert (api_response['products'][1]["in_stock"]) != -1
    assert (api_response['products'][1]["in_stock"]) != True
    assert (api_response['products'][2]["in_stock"]) == True
    assert (api_response['products'][2]["in_stock"]) != "True"
    assert (api_response['products'][2]["in_stock"]) != 200.4949
    assert (api_response['products'][2]["in_stock"]) != -2199
    assert (api_response['products'][2]["in_stock"]) != False

def test_HTTP_status_codes():
    # Finally, we'll test the HTTP status codes, using positive and negative testing:
    assert (api_response['HTTP_Status_Codes'][0]["200"]) == "Success. The request has succeeded."
    assert (api_response['HTTP_Status_Codes'][0]["200"]) != "True"
    assert (api_response['HTTP_Status_Codes'][0]["200"]) != 23.1838395
    assert (api_response['HTTP_Status_Codes'][0]["200"]) != -52.1838395
    assert (api_response['HTTP_Status_Codes'][0]["200"]) != True
    assert (api_response['HTTP_Status_Codes'][0]["200"]) != False
    assert (api_response['HTTP_Status_Codes'][0]["400"]) == "Bad Request. The server could not understand the request due to invalid syntax."
    assert (api_response['HTTP_Status_Codes'][0]["400"]) != "False"
    assert (api_response['HTTP_Status_Codes'][0]["400"]) != 20.7844235234
    assert (api_response['HTTP_Status_Codes'][0]["400"]) != -144906
    assert (api_response['HTTP_Status_Codes'][0]["400"]) != True
    assert (api_response['HTTP_Status_Codes'][0]["400"]) != False
    assert (api_response['HTTP_Status_Codes'][0]["401"]) == "Unauthorized. The request requires user authentication or, if the request included authorization credentials, authorization has been refused for those credentials."
    assert (api_response['HTTP_Status_Codes'][0]["401"]) != "True"
    assert (api_response['HTTP_Status_Codes'][0]["401"]) != 24500.4949
    assert (api_response['HTTP_Status_Codes'][0]["401"]) != -219.229
    assert (api_response['HTTP_Status_Codes'][0]["401"]) != True
    assert (api_response['HTTP_Status_Codes'][0]["401"]) != False
    assert (api_response['HTTP_Status_Codes'][0]["404"]) == "Not Found. The server has not found anything that matches the Request-URI."
    assert (api_response['HTTP_Status_Codes'][0]["404"]) != "False"
    assert (api_response['HTTP_Status_Codes'][0]["404"]) != 20.784543
    assert (api_response['HTTP_Status_Codes'][0]["404"]) != -195
    assert (api_response['HTTP_Status_Codes'][0]["404"]) != True
    assert (api_response['HTTP_Status_Codes'][0]["404"]) != False
    assert (api_response['HTTP_Status_Codes'][0]["500"]) == "Internal Server Error. The server encountered an unexpected condition which prevented it from fulfilling the request."
    assert (api_response['HTTP_Status_Codes'][0]["500"]) != "True"
    assert (api_response['HTTP_Status_Codes'][0]["500"]) != 200.494955
    assert (api_response['HTTP_Status_Codes'][0]["500"]) != -.000000234524112199
    assert (api_response['HTTP_Status_Codes'][0]["500"]) != True
    assert (api_response['HTTP_Status_Codes'][0]["500"]) != False