import requests
import json
import os

token = os.environ.get('TOKEN')
response = requests.get('https://api.github.com/user',
                         headers={'Authorization':f'token {token}'})

content = response.content.decode('utf-8')
user = json.loads(content)

print(user)