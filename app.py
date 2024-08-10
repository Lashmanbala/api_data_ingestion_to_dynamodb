import requests
import json
import os

token = os.environ.get('TOKEN')
# response = requests.get('https://api.github.com/user',
                        #  headers={'Authorization':f'token {token}'})

# content = response.content.decode('utf-8')
# user = json.loads(content)

# repo_res = requests.get('https://api.github.com/repos/lashmanbala/api_data_ingestion_to_dynamodb',
        # headers = {'Authorization':f'token {token}'})

# repos = json.loads(repo_res.content.decode('utf-8'))

repos_res = requests.get('https://api.github.com/repositories?since=840563886',headers = {'Authorization':f'token {token}'})

repos = json.loads(repos_res.content.decode('utf-8'))
               
repo_details = []

for repo in repos:
    try:
        owner = repo['owner']['login']
        name = repo['name']

        rd = json.loads(requests.get(f'https://api.github.com/repos/{owner}/{name}', headers={'Authorization':f'token {token}'}).content.decode('utf-8'))

        repo_detail = {'id': rd['id'],
                        'node_id': rd['node_id'],
                        'name': rd['name'],
                        'full_name': rd['full_name'],
                        'owner': {
                            'login': rd['owner']['login'],
                            'id': rd['owner']['id'],
                            'node_id': rd['owner']['node_id'],
                            'type': rd['owner']['type'],
                            'site_admin': rd['owner']['site_admin']
                            },
                        'html_url': rd['html_url'],
                        'description': rd['description'],
                        'fork': rd['fork'],
                        'created_at': rd['created_at']
                        }

        repo_details.append(repo_detail)
    except:
        pass

print(len(repo_details))
