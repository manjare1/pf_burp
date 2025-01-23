import os
from dotenv import load_dotenv

load_dotenv()

NAME=os.getenv('NAME')
TICKER=os.getenv('TICKER')
TEXT=os.getenv('TEXT')
FILE=os.getenv('FILE')
AMOUNT=os.getenv('AMOUNT')
