import logging
import random
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
import requests

API_TOKEN = '5611180900:AAEmIEV24S75SGXog4T9wMTxlBixLeIGOGI'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware()) #для безопастности  


'''*************Клиентская часть****************'''

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.message):
    try:
        await bot.send_message(message.from_user.id, 'Приятного аппетита!')
        await message.delete()

    except:
        message.reply('Общение с ботом')

@dp.message_handler(commands=['Режим_работы'])
async def resto_open_command(message:types.message):
    shedule_restorant = \
    '''
    пн-пт: 9-00 по 18-00
    сб-вс: 15-00 по 22-00
    '''
    await bot.send_message(message.from_user.id, shedule_restorant)



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)