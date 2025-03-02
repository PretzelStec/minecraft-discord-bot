import boto3
from ...config.appConfig import appConfig

class SES:
    def __init__(self):
        self.client = boto3.client(
            'ses',
            region_name='us-east-1',
            aws_access_key_id=appConfig.AWS_ACCESS_KEY,
            aws_secret_access_key=appConfig.AWS_SECRET_ACCESS_KEY
        )

    def sendSimpleEmail(self, recipient, message):
        self.client.send_email(
            Source=appConfig.ALERT_SOURCE_EMAIL,
            Destination={
                'ToAddresses': [recipient],
            },
            Message={
                'Subject': {
                    'Data': message,
                    'Charset': 'utf-8'
                },
                'Body': {
                    'Text': {
                        'Data': message,
                        'Charset': 'utf-8'
                    }
                }
            }
        )

ses = SES()