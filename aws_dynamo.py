import os
import boto3
from botocore.exceptions import ClientError

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
        print('ghrepos table successfully created')
    
    except ClientError as e:
        if e.response['Error']['Code'] == 'ResourceInUseException':
            print("Table 'ghrepos' already exists.")
        else:
            print(f"Unexpected error: {e}")

    try:
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

        print('Marker table created successfully')

    except ClientError as e:
        if e.response['Error']['Code'] == 'ResourceInUseException':
            print("Table 'ghmarker' already exists.")
        else:
            print(f"Unexpected error: {e}")


def load_repos(table_name, repo_details_list):
    try:
        batch_size = 25
        batch_items = []
        batch_number = 1

        for repo in repo_details_list:
            # Convert the item attributes to the correct DynamoDB format
            item = {
                'PutRequest': {
                    'Item': {
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
                }
            }

            batch_items.append(item)

            # Once batch_items reaches the batch_size limit, write the items to DynamoDB
            if len(batch_items) == batch_size:
                dynamo_db.batch_write_item(RequestItems={table_name: batch_items})
                print(f'Successfully inserted batch {batch_number}')
                batch_number += 1
                batch_items = []  # Reset batch_items after writing

        # Write any remaining items that were not written in the last batch
        if batch_items:
            dynamo_db.batch_write_item(RequestItems={table_name: batch_items})
            print(f'Successfully inserted final batch {batch_number}')

    except Exception as e:
        print(f'Error: {e}')

               

# response = dynamo_db.scan(
#     TableName='ghrepos')
# print(response)