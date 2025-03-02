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
        self.GLOBAL_CHANNEL_NAME = os.getenv('GLOBAL_CHANNEL_NAME')

appConfig = AppConfig()