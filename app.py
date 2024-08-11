import os
from util import list_repos, get_repos
from aws_dynamo import load_repos, create_tables


token = os.environ.get('TOKEN')

repos = list_repos(token)
repos_details = get_repos(repos, token)
print(len(repos_details))
table_name = 'ghrepos'
load_repos(table_name, repos_details)

