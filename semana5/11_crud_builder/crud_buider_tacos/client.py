import requests

url = "http://localhost:8000/pizzas"
headers = {'Content-type': 'application/json'}

# GET /tacos
response = requests.get(url)
print(response.json())

# POST /tacos 
mi_taco = {
    "base ": "Grande",
    "guiso": "Delgada",
    "toppings": ["Jamon", "Queso"],
    "salsa": "Delgada"
}
response = requests.post(url, json=mi_taco, headers=headers)
print(response.json())

# GET /tacos
response = requests.get(url)
print(response.json())

# PUT /tacos/1
edit_taco = {
    "tamaño": "Mediano",
    "masa": "Gruesa",
    "toppings": ["Pepperoni", "Queso"],
    "salsa": "Delgada"
}
response = requests.post(url, json=edit_taco, headers=headers)
print(response.json())

# GET /taco
response = requests.get(url)
print(response.json())

# DELETE /taco/1

response = requests.delete(url + "/1")
print(response.json())

# GET /tacos
response = requests.get(url)
print(response.json())