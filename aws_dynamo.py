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

        print('Tables created successfully')
    except Exception as e:
        print(e)

