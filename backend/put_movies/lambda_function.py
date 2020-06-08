import boto3
from random import randint
import os
import json


def persist_to_dynamo(item: dict):
    client = boto3.client('dynamodb')
    table_name = os.getenv("TABLE_NAME", "ServerlessDemo")
    response = client.put_item(
        TableName=table_name,
        Item = item
    )
    return response


def lambda_handler(event, context):
    generate_random_id =  randint(323, 11999)
    json_body = json.loads(event['body'])
    print(type(json_body))
    
    try:
        movie_name_strp = json_body.get("movie_name").replace(" ", "")
        movie_name = json_body.get("movie_name")
        movie_description = json_body.get("description")
        
        movie_id = f"{movie_name_strp}{generate_random_id}"
    
        item = {
            "movie_id" : {'S': movie_id},
            "movie_name" : {'S': movie_name},
            "description": {'S': movie_description}
        }
        print(item)
        result = persist_to_dynamo(item)
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
            },
            'body': json.dumps(result)
        }
    except Exception as e:
        raise e
