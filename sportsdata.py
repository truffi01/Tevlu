import requests 
import json 

req = requests.get('https://jsonplaceholder.typicode.com/todos/1')

print(req.text)

