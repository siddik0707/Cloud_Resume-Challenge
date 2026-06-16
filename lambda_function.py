import json
import boto3

table = boto3.resource('dynamodb').Table('cloud-resume-db')

def lambda_handler(event, context):

    response = table.update_item(
        Key={'id': 'visitors'},
        UpdateExpression='ADD #c :inc',
        ExpressionAttributeNames={
            '#c': 'count'
        },
        ExpressionAttributeValues={
            ':inc': 1
        },
        ReturnValues='UPDATED_NEW'
    )

    count = int(response['Attributes']['count'])

    return {
    "statusCode": 200,
    "headers": {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Headers": "Content-Type",
        "Access-Control-Allow-Methods": "GET,OPTIONS"
    },
    "body": json.dumps({
        "visitorCount": count
    })
}
