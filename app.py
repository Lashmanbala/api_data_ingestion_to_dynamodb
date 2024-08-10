import requests
import json
import os

token = os.environ.get('TOKEN')
response = requests.get('https://api.github.com/user',
                         headers={'Authorization':f'token {token}'})

content = response.content.decode('utf-8')
user = json.loads(content)

repo_res = requests.get('https://api.github.com/repos/lashmanbala/api_data_ingestion_to_dynamodb',
        headers = {'Authorization':f'token {token}'})

repos = json.loads(repo_res.content.decode('utf-8'))

repos_list = requests.get('https://api.github.com/repositories?since=840563886',headers = {'Authorization':f'token {token}'})

lst = json.loads(repos_list.content.decode('utf-8'))

print(len(lst))
