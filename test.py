import requests

url = "http://34.209.240.233//api/v1/books/40"


response = requests.get(url)
print(response)
print(response.json())