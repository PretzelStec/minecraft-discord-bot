import boto3
from ..config.appConfig import appConfig

class EC2:
    def __init__(self):
        self.client = boto3.client(
            'ec2',
            region_name='us-east-1',
            aws_access_key_id=appConfig.AWS_ACCESS_KEY,
            aws_secret_access_key=appConfig.AWS_SECRET_ACCESS_KEY
        )

        self.instanceIds = ["i-0fc7e9bc7e962cdda"]
    
    def startInstances(self):
        self.client.start_instances(InstanceIds=self.instanceIds)

    def stopInstances(self):
        self.client.stop_instances(InstanceIds=self.instanceIds)

    def getInstanceStatus(self):
        reservations = self.client.describe_instances(InstanceIds=self.instanceIds).get("Reservations")
        status = ''

        for reservation in reservations:
            for instance in reservation['Instances']:
                status = instance.get('State').get('Name')

        return status

ec2 = EC2()