import os

BOT_TOKEN = os.environ['NEWCOINS_BOT_TOKEN']
BOT_NAME = 'NewCoinsNotifyBot'

DATABASE_URL = os.environ['DATABASE_URL']

CHECK_INTERVAL = int(os.environ['NEWCOINS_BOT_CHECK_INTERVAL'])  # seconds

CHANNEL_ID = os.environ['NEWCOINS_BOT_CHANNEL_ID']
