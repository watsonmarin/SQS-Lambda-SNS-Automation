import json 
import boto3 
import os 
 
def lambda_handler(event, context): 
    batch_processes=[] 
    for record in event['Records']: 
        send_request(record["body"]) 
 
 
def send_request(body): 
    # Create an SNS client 
    sns = boto3.client('sns') 
 
    # Publish a simple message to the specified SNS topic 
    response = sns.publish( 
        TopicArn="arn:aws:sns:us-west-2:464599248654:JJTech-Test-Delete", 
        Message=body, 
    ) 
 
    # Print out the response 
    print(response) 
