import requests
url = "http://localhost:8000"

#GET
response = requests.get(f"{url}/posts")

print(response.text)

