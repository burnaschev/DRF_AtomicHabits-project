import requests
from django.conf import settings

def get_telegram_updates(offset=None):
    url = f'https://api.telegram.org/bot{settings.TELEGRAM_BOT_API_KEY}/getUpdates'
    params = {'offset': offset} if offset else {}
    response = requests.get(url, params=params)
    return response.json()




