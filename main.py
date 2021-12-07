print("Hello world from Alex")

import requests

payload = {'name': 'test'}
response = requests.get("https://playground.learnqa.ru/api/hello", params=payload)
print(response.text)