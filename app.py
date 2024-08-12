import os
from util import list_repos, get_repos
from aws_dynamo import load_repos, create_tables

def main():
    token = os.environ.get('TOKEN')

    # Creating tables
    create_tables()

    since_repo_id = 840563986     # from this repo, the app gets list of 100 repos
    repos = list_repos(token, since_repo_id)
    repos_details = get_repos(repos, token) # getting details of each repo
    print(f'N.of valid repos collectd {len(repos_details)}')

    table_name = 'ghrepos'
    load_repos(table_name, repos_details) # uploading the collected repo details into documentDb

if __name__ == "__main__":
    main()
