from discord import Status, Game
from discord.ext import tasks
from datetime import datetime

from source.config.appConfig import appConfig
from source.domain.getServerStatus import getServerStatus
from source.infrastructure.aws.s3 import s3


@tasks.loop(seconds=appConfig.SERVER_BACKUP_TASK_RATE)
async def serverBackup():
    print("Initiating server backup...")
    status = await getServerStatus()

    if(status.status == 0):
        print('Server detected offline... skipping backup..')
        return
    
    # Clear the S3 bucket.
    print("Clearning the s3 bucket...")
    await s3.clearBucket(appConfig.AWS_S3_BUCKET_NAME)
    print("S3 bucket cleared.")

    # Zip the server directory.
    folderToZip = appConfig.PATH_TO_SERVER
    print(f"Zipping folder: {folderToZip}")
    if not os.path.exists(folderToZip):
        print(f"Error: The folder {folderToZip} does not exist.")
        return

    zipPath = f'server-backup-{datetime.now().isoformat()}.zip'
    zipFolder(folderToZip, zipPath)

    # Upload the zipped file to S3.
    await s3.uploadFile(zipPath, appConfig.AWS_S3_BUCKET_NAME, zipPath)

    print("Server backup complete.")

    return

import zipfile
import os

def zipFolder(folderPath, zipPath):
    with zipfile.ZipFile(zipPath, "w", zipfile.ZIP_DEFLATED) as zip:
        for root, _, files in os.walk(folderPath):
            for file in files:
                filePath = os.path.join(root, file)
                zip.write(filePath, os.path.relpath(filePath, folderPath))
