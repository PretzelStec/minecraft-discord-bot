from dotenv import load_dotenv
load_dotenv()

import os

class AppConfig:
    def __init__(self):
        self.DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
        self.AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
        self.AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
        self.ALERT_RECIPIENT = os.getenv('ALERT_RECIPIENT')
        self.ALERT_SOURCE_EMAIL = os.getenv('ALERT_SOURCE_EMAIL')
        self.MINECRAFT_SERVER_URL = os.getenv('MINECRAFT_SERVER_URL')
        self.MINECRAFT_SERVER_PORT = int(os.getenv('MINECRAFT_SERVER_PORT'))
        self.AUTO_SHUTDOWN_TASK_TIMER = int(os.getenv('AUTO_SHUTDOWN_TASK_TIMER'))
        self.POLL_STATUS_TASK_RATE = int(os.getenv('POLL_STATUS_TASK_RATE'))
        self.SERVER_BACKUP_TASK_RATE = int(os.getenv('SERVER_BACKUP_TASK_RATE'))
        self.PATH_TO_SERVER = os.getenv('PATH_TO_SERVER')
        self.GLOBAL_CHANNEL_NAME = os.getenv('GLOBAL_CHANNEL_NAME')
        self.AWS_S3_BUCKET_NAME = os.getenv('AWS_S3_BUCKET_NAME')
        self.IS_BACKUP_ENABLED = bool(os.getenv('IS_BACKUP_ENABLED') == "true")
        self.IS_POLLING_ENABLED = bool(os.getenv('IS_POLLING_ENABLED') == "true")

appConfig = AppConfig()