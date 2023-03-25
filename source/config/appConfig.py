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

appConfig = AppConfig()