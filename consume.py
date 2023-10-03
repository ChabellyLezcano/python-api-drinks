import requests

response = requests.get('27.0.0.1:8000/drinks')
print(response.json())