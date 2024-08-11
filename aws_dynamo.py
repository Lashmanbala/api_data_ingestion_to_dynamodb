import os
import boto3

dynamo_db = boto3.client('dynamodb')

def create_tables():
    try:
        ghrepos_table = dynamo_db.create_table(
            TableName='ghrepos',
            AttributeDefinitions=[
                {
                    'AttributeName': 'id',
                    'AttributeType': 'N'    # Numeric
                },
            ],
            KeySchema=[
                {
                    'AttributeName': 'id',
                    'KeyType': 'HASH'
                },
            ],
            BillingMode='PAY_PER_REQUEST'
        )
        print(ghrepos_table)

        marker_table = dynamo_db.create_table(
            TableName='ghmarker',
            AttributeDefinitions=[
                {
                    'AttributeName': 'tn',
                    'AttributeType': 'S'    # String
                },
            ],
            KeySchema=[
                {
                    'AttributeName': 'tn',
                    'KeyType': 'HASH'
                },
            ],
            BillingMode='PAY_PER_REQUEST'
        )

        print(marker_table)
        print('Tables created successfully')
    except Exception as e:
        print(e)


def load_repos(table_name, repo_details_list):
    for repo in repo_details_list:
        # Convert the item attributes to the correct DynamoDB format
        item = {
            'id': {'N': str(repo['id'])},  # 'N' for Number, must be a string representation of the number
            'node_id': {'S': repo['node_id']},  # 'S' for String
            'name': {'S': repo['name']},
            'full_name': {'S': repo['full_name']},
            'owner': {
                'M': {  # 'M' for Map
                    'login': {'S': repo['owner']['login']},
                    'id': {'N': str(repo['owner']['id'])},
                    'node_id': {'S': repo['owner']['node_id']},
                    'type': {'S': repo['owner']['type']},
                    'site_admin': {'BOOL': repo['owner']['site_admin']}  # 'BOOL' for Boolean
                }
            },
            'html_url': {'S': repo['html_url']},
            'description': {'S': repo['description'] or ''},  # Handle None by providing an empty string
            'fork': {'BOOL': repo['fork']},
            'created_at': {'S': repo['created_at']}
        }

        try:
            dynamo_db.put_item(
                TableName=table_name,
                Item=item
            )
        except Exception as e:
            print(f"Failed to insert item: {e}")

    print('Successfully uploaded into table')

response = dynamo_db.scan(
    TableName='ghrepos')
print(response)