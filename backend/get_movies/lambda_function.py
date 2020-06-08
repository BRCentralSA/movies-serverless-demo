import boto3
from random import randint
import os
import json


def deserializer(items):
    boto3.resource('dynamodb')
    # To go from low-level format to python
    deserializer = boto3.dynamodb.types.TypeDeserializer()
    python_data = {k: deserializer.deserialize(v) for k,v in items.items()}
    return python_data


def get_dynamo_items():
    client = boto3.client('dynamodb')
    table_name = os.getenv("TABLE_NAME", "ServerlessDemo")
    response = client.scan(
        TableName=table_name,
    )
    return response


def lambda_handler(event, context):
    try:
        result = get_dynamo_items().get("Items")
        movie_list = []

        for items in result:
            new_item = deserializer(items)
            movie_list.append(new_item)

        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
            },
            'body': json.dumps(movie_list)
        }
    except Exception as e:
        raise e