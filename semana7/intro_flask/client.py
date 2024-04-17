import requests

url = 'http://localhost:5000/'

# Saludar
params_saludar = {'nombre': 'Miguel_Angel'}
response_saludar = requests.get(url + 'saludar', params=params_saludar)
if response_saludar.status_code == 200:
    data_saludar = response_saludar.json()
    mensaje_saludar = data_saludar['mensaje']
    print("Respuesta del servidor (GET):", mensaje_saludar)
else:
    print("Error al conectar con el servidor (GET - Saludar):", response_saludar.status_code)

# Sumar dos números
payload_sumar = {'num1': 5, 'num2': 3}
response_sumar = requests.post(url + 'sumar', json=payload_sumar)
if response_sumar.status_code == 200:
    data_sumar = response_sumar.json()
    resultado_sumar = data_sumar['resultado']
    print("Resultado de la suma:", resultado_sumar)
else:
    print("Error al conectar con el servidor (Sumar):", response_sumar.status_code)

# Verificar si una cadena es un palíndromo
payload_palindromo = {'cadena': 'reconocer'}
response_palindromo = requests.post(url + 'palindromo', json=payload_palindromo)
if response_palindromo.status_code == 200:
    data_palindromo = response_palindromo.json()
    mensaje_palindromo = data_palindromo['mensaje']
    print("Respuesta del servidor (Palíndromo):", mensaje_palindromo)
else:
    print("Error al conectar con el servidor (Palíndromo):", response_palindromo.status_code)

# Contar una vocal en una cadena
payload_contar = {'cadena': 'excepciones', 'vocal': 'e'}
response_contar = requests.post(url + 'contar', json=payload_contar)
if response_contar.status_code == 200:
    data_contar = response_contar.json()
    resultado_contar = data_contar['resultado']
    print("Número de veces que aparece la vocal 'e':", resultado_contar)
else:
    print("Error al conectar con el servidor (Contar):", response_contar.status_code)
