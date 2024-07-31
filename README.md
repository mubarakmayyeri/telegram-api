# Telegram Message Sender

This Python script sends formatted messages to a Telegram channel using the Telegram Bot API. The script reads the bot token and channel ID from environment variables stored in a `.env` file.

## Features

- Sends messages to a Telegram channel
- Supports Markdown and HTML formatting
- Reads sensitive information from environment variables

## Requirements

- Python 3.x
- `requests` library
- `python-dotenv` library

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/telegram-message-sender.git
    cd telegram-message-sender
    ```

2. **Create a virtual environment** (optional but recommended):
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages**:
    ```sh
    pip install requests python-dotenv
    ```

4. **Create a `.env` file** in the root directory of the project and add your Telegram bot token and channel ID:
    ```env
    TELEGRAM_TOKEN=YOUR_TOKEN_HERE
    TELEGRAM_CHANNEL_ID=@your_channel_id
    ```

## Usage

1. **Modify the script if necessary**: Update the `message` variable in `send_message.py` with the message you want to send.

2. **Run the script**:
    ```sh
    python send_message.py
    ```

## Example Script

```python
import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the token and channel ID from environment variables
TOKEN = os.getenv('TELEGRAM_TOKEN')
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
```