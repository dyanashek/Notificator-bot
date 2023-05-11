import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

# keywords and problem
keywords = {
    '-((1))-' : 'оплата',
    '-((2))-' : 'проблема',
    '-((3))-' : 'конфликт',
}

# managers id
DIRECTOR_ID = '5316876288'