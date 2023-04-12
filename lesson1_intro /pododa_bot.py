import logging
import random
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
import requests

API_TOKEN = '6294917742:AAHBSSRu1oX4GTCVLYjzpMtyyW6e-PuTfRA'
api_pogoda = '97c07b89b662c8012dabe09ef310a2a7'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware()) #для безопастности  

def weather(city):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_pogoda}&units=metric'
    response = requests.get(url)

    data = response.json()
    
    if data['cod'] != '404':
        main = data['main']
        weather_desc = data['weather'][0]['description'].capitalize()
        temperature = main['temp']
        humidity = main['humidity']
        wind_speed = data['wind']['speed']
        return f'Погода в городе {city.title()}: \
            \n{weather_desc}\
            \nТемпература: {temperature} C\
            \nВлажность: {humidity} %\
            \nСкорость ветра: {wind_speed} м/с'
    else:
        return f'Город {city.capitalize()} не был найден!'


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.message):
    await message.reply('Привет, друг! Я бот, который показывает погоду!')


@dp.message_handler(commands=['weather'])
async def send_weater(message: types.message):
    text_part = message.text.split('/weather ')
    if len(text_part) < 2:
        await message.reply("Пожайлуста пишите название города рядом с коммандой weather пример: \'/weather Bishkek'")
        return
    city = text_part[1]
    weather_info = weather(city.capitalize())
    await message.reply(weather_info)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

