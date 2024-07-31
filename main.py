import requests
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
CHANNEL_ID = os.getenv('TELEGRAM_CHANNEL_ID')

def send_message(token, channel_id, message, parse_mode='Markdown'):
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    payload = {
        'chat_id': channel_id,
        'text': message,
        'parse_mode': parse_mode
    }
    response = requests.post(url, data=payload)
    return response.json()

if __name__ == "__main__":
    message = "**Hello**, this is a *test* message with `formatted` text!"
    response = send_message(TOKEN, CHANNEL_ID, message)
    print(response)
