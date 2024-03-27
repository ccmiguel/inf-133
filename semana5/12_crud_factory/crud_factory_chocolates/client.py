import requests
import json

url = "http://localhost:8000/chocolates"
headers = {"Content-Type": "application/json"}

# POST /deliveries
new_chocolate_data = {
    "chocolate_type": "bombon",
    "peso": 50,
    "sabor": "Vainilla",
    "relleno": "Fresa"   
}
response = requests.post(url=url, json=new_chocolate_data, headers=headers)
print(response.json())

new_chocolate_data = {
    "chocolate_type": "trufa",
    "peso": 10,
    "sabor": "Almendra",
    "relleno": "Durazno" 
}
response = requests.post(url=url, json=new_chocolate_data, headers=headers)
print(response.json())


# GET /deliveries
response = requests.get(url=url)
print(response.json())

# PUT /deliveries/{vehicle_id}
chocolate_id_to_update = 1
updated_chocolate_data = {
    "peso": "89"
}
response = requests.put(f"{url}/{chocolate_id_to_update}", json=updated_chocolate_data)
print("Chocolate actualizado:", response.json())

# GET /deliveries
response = requests.get(url=url)
print(response.json())

# DELETE /deliveries/{chocoloate_id}
chocolate_id_to_delete = 1
response = requests.delete(f"{url}/{chocolate_id_to_delete}")
print("Chocolate eliminado:", response.json())

# GET /deliveries
response = requests.get(url=url)
print(response.json())