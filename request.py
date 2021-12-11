import requests
import json

response = requests.get('https://simple-books-api.glitch.me/books')

for i in range(0, len(response.json())):
	print(response.json()[i]['name'])