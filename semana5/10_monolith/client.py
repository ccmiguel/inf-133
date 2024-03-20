import requests

#GET
url = "http://localhost:8000"
response = requests.get(f"{url}/posts")
print(response.text)

#GET por id
response = requests.get(f"{url}/post/2")
print(response.text)

#POST
json = {
    1: {
        "title": "Mi experiencia como dev",
        "content": "¡Hola mundo! Esta es mi primera experiecia como dev.",
    },
    2: {
        "title": "Otra publicación",
        "content": "¡Bienvenidos a mi blog! Aquí hay otra publicación.",
    },
}
response = requests.get(f"{url}/posts", data=json)
print(response.text)

#put
put_data = {
    1: {
        "title": "Mi experiencia como estudiante de la UMSA",
        "content": "¡Hola mundo! Esta es mi primera experiecia como estudiante.",
    }
}
response = requests.put(f"{url}/posts", data=put_data)
print(response.text)

#delete
response = requests.delete(f"{url}/post/2")
print(response.text)

