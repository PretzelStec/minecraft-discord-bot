import asyncio
from concurrent.futures import ThreadPoolExecutor
import boto3

from ...config.appConfig import appConfig


class S3:
    def __init__(self):
        self.client = boto3.client(
            's3',
            region_name='us-east-1',
            aws_access_key_id=appConfig.AWS_ACCESS_KEY,
            aws_secret_access_key=appConfig.AWS_SECRET_ACCESS_KEY
        )
        self.executor = ThreadPoolExecutor(max_workers=3)

    async def uploadFile(self, filePath, bucketName, key):
        loop = asyncio.get_event_loop()
        try:
            await loop.run_in_executor(self.executor, self.client.upload_file, filePath, bucketName, key)
        except:
            print("Failed to upload file to S3.")
            raise

    async def clearBucket(self, bucketName):
        print(f"Clearing bucket {bucketName}...")
        loop = asyncio.get_event_loop()
        try:
            # List all objects in the bucket
            response = await loop.run_in_executor(self.executor, lambda: self.client.list_objects_v2(Bucket=bucketName))
            if 'Contents' in response:
                objects = [{'Key': obj['Key']} for obj in response['Contents']]
                # Delete all objects in the bucket
                await loop.run_in_executor(self.executor, lambda: self.client.delete_objects(Bucket=bucketName, Delete={'Objects': objects}))
                print(f"Cleared all objects in bucket {bucketName}.")
            else:
                print(f"No objects found in bucket {bucketName}.")
        except:
            print("Failed to clear bucket.")
            raise

s3 = S3()