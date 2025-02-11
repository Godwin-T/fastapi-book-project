import requests

url = "http://52.24.79.29//api/v1/books/1"
response = requests.get(url)
print(response)
print(response.json())