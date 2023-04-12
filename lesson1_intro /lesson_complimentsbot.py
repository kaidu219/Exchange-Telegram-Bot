import logging
import random
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware

API_TOKEN = '5558634678:AAH-WKVp-6HVbT5OJLKTK4gBapRr3QUsWlA'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware()) #для безопастности 

comparisons = [    
    "У тебя бег как у осла.",    
    "Ты настойчив как собака.",    
    "Ты красива, как желудь.",    
    "Твой нюх острее, чем нож.",    
    "Ты быстро скачешь, словно корова.",    
    "Ты тих, как армагедон.",    
    "Твой голос сладкий, как у картошки.",    
    "Ты так терпелив, как деньги.",    
    "Ты легкая, как камень.",    
    "Твои зубы острые, как часы.",
    "Ты ленива, как ты.",   
    "Ты хитер, как жаба.",    
    "Ты крепкая, как маршрутка.",    
    "Ты громкий, как ступня.",    
    "Ты мила, как петух.",    
    "Ты сильный, как ключ.",    
    "Ты легкая на подъем, как камень в душе.",    
    "Ты быстрый, жаль что везде.",    
    "Ты грациозная, как ты в зеркале.",    
    "Ты упрямый, как луна."
    ]
somelist = [
    'Ты даун? Набери /compliment'
]

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.message):
    await message.reply('Привет друг! Я бот, который делает комплементы! /compliment')

@dp.message_handler(commands=['compliment'])
async def make_compliment(message: types.message):
    compliment = random.choice(comparisons)
    await message.reply(compliment)

@dp.message_handler()
async def make_compliment(message: types.message):
    compliment = random.choice(somelist)
    await message.reply(compliment)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)