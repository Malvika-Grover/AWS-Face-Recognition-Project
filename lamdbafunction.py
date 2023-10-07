from __future__ import print_function

import boto3
from decimal import Decimal
import json
import urllib

print('Loading function')

dynamodb = boto3.client('dynamodb')
s3 = boto3.client('s3')
rekognition = boto3.client('rekognition')

# --------------- Helper Functions ------------------

def index_faces(bucket, key):
    try:
        response = rekognition.index_faces(
            Image={"S3Object": {"Bucket": bucket, "Name": key}},
            CollectionId="facerecognition_collection"
        )
        print("Index Faces Response:", response)
        return response
    except Exception as e:
        print("Error in index_faces:", e)
        raise e

def update_index(tableName, faceId, fullName):
    try:
        response = dynamodb.put_item(
            TableName=tableName,
            Item={
                'RekognitionId': {'S': faceId},
                'FullName': {'S': fullName}
            }
        )
        print("Update Index Response:", response)
        return response
    except Exception as e:
        print("Error in update_index:", e)
        raise e

# --------------- Main handler ------------------

def lambda_handler(event, context):
    # Print the entire event for troubleshooting
    print("Event: ", event)

    # Get the object from the event
    records = event.get('Records', [])
    if not records:
        print("No records found in the event.")
        return

    bucket = records[0].get('s3', {}).get('bucket', {}).get('name', '')
    key = records[0].get('s3', {}).get('object', {}).get('key', '')

    try:
        # Calls Amazon Rekognition IndexFaces API to detect faces in S3 object
        # to index faces into specified collection
        response = index_faces(bucket, key)

        # Commit faceId and full name object metadata to DynamoDB
        if response and response['ResponseMetadata']['HTTPStatusCode'] == 200:
            faceId = response['FaceRecords'][0]['Face']['FaceId']

            ret = s3.head_object(Bucket=bucket, Key=key)
            personFullName = ret['Metadata']['fullname']

            update_index('facerecognition', faceId, personFullName)

        # Print response to console
        print("Lambda Handler Response:", response)

        return response
    except Exception as e:
        print(e)
        print("Error processing object {} from bucket {}. ".format(key, bucket))
        raise e
