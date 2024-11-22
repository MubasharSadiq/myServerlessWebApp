import json
import boto3

# Initialize DynamoDB and SES
dynamodb = boto3.resource('dynamodb', region_name='eu-west-1')  # Update with your region
table = dynamodb.Table('contacts')
ses = boto3.client('ses')

def lambda_handler(event, context):
    try:
        # Scan the DynamoDB table
        result = table.scan()
        items = result.get('Items', [])

        if not items:
            return {
                'statusCode': 400,
                'body': json.dumps('No contact information found.')
            }

        # Sort items to get the latest entry
        items.sort(key=lambda x: x['timestamp'], reverse=True)
        latest_contact = items[0]
        
        # Format the email body
        body = f"""
        Contact Information:
        Timestamp: {latest_contact['timestamp']}
        Name: {latest_contact['name']}
        Email: {latest_contact['email']}
        Message: {latest_contact['message']}
        """

        # Send email
        ses.send_email(
            Source='<FROM_EMAIL>',  # Replace with your verified SES email address
            Destination={
                'ToAddresses': [latest_contact['email']]  # Send to the contact email
            },
            Message={
                'Subject': {
                    'Data': 'Thank You for Your Message!',
                    'Charset': 'UTF-8'
                },
                'Body': {
                    'Text': {
                        'Data': body,
                        'Charset': 'UTF-8'
                    }
                }
            }
        )

        return {
            'statusCode': 200,
            'body': json.dumps('Email successfully sent!')
        }

    except Exception as e:
        print(f"Error: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error sending email: {str(e)}")
        }