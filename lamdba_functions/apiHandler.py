import json
import datetime
import random
import boto3

client = boto3.client('kinesis')


def lambda_handler(event, context):
    # TODO implement
    print(event)
    data = json.dumps(event['body'])  
    client.put_record(StreamName="sampleDataStreamKinesis", Data=data, PartitionKey="1")
    print("Data Inserted")
    return data