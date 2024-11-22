import json
import boto3
from datetime import datetime

def lambda_handler(event, context):
    # Connect to DynamoDB table
    db = boto3.resource('dynamodb')
    table = db.Table('Contacts') # Update with your DynamoDB table name
    
    # Create timestamp
    dateTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    try:
        # Get contact info from request
        payload = json.loads(event['body'])
        
        # Add row with contact info to DynamoDB
        table.put_item(
            Item={
                'timestamp': dateTime,
                'name': payload['name'],
                'email': payload['email'],
                'message': payload['message']
            }
        )
        
        # Return success response
        return {
            'statusCode': 200,
            'body': json.dumps('Successfully saved contact info!'),
            'headers': {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Credentials": True,
            }
        }
    
    except Exception as e:
        # Log error and return error response
        print(f"Error: {e}")
        return {
            'statusCode': 400,
            'body': json.dumps('Error saving contact info'),
            'headers': {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Credentials": True,
            }
        }