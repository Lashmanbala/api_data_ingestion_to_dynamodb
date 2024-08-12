import requests
import json

def list_repos(token, since_repo_id):
    repos_res = requests.get(f'https://api.github.com/repositories?since={since_repo_id}',
                             headers = {'Authorization':f'token {token}'})
    
    return json.loads(repos_res.content.decode('utf-8'))


def get_repo_details(owner, name, token):
    repo_details = json.loads(requests.get(f'https://api.github.com/repos/{owner}/{name}', 
                                          headers={'Authorization':f'token {token}'}
                                          ).content.decode('utf-8'))

    return repo_details

def extract_repo_fields(repo_details):
    repo_fields = {'id': repo_details['id'],
                    'node_id': repo_details['node_id'],
                    'name': repo_details['name'],
                    'full_name': repo_details['full_name'],
                    'owner': {
                        'login': repo_details['owner']['login'],
                        'id': repo_details['owner']['id'],
                        'node_id': repo_details['owner']['node_id'],
                        'type': repo_details['owner']['type'],
                        'site_admin': repo_details['owner']['site_admin']
                        },
                    'html_url': repo_details['html_url'],
                    'description': repo_details['description'],
                    'fork': repo_details['fork'],
                    'created_at': repo_details['created_at']
                    }
    return repo_fields

def get_repos(repos, token):
    repos_details = []
    
    for repo in repos:
        try:
            owner = repo['owner']['login']
            name = repo['name']

            repo_details = get_repo_details(owner, name, token)
            repo_fields = extract_repo_fields(repo_details)
            repos_details.append(repo_fields)
        except:
            pass
        
    return repos_details