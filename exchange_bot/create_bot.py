import logging
import random
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
import requests
import os

API_TOKEN = '6287041999:AAGUysFBMJEZ01JQOkb1KoKs8m7Hi5QaF1I'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware()) #для безопастности  