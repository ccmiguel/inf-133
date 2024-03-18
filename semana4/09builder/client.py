import requests

url = "http://localhost:8000/pizza"
headers = {'Content-type': 'application/json'}

mi_pizza = {
    "tamaño": "Grande",
    "masa": "Delgada",
    "toppings": ["Jamon", "Queso"]
}
t_pizza = {
    "tamaño": "Mediana",
    "masa": "Gruesa",
    "toppings": ["Peperoni", "Pinia"]
}
response = requests.post(url, json=mi_pizza, headers=headers)
response2 = requests.post(url, json=t_pizza, headers=headers)
print(response.json())
print(response2.json())