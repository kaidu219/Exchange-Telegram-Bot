from aiogram import types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from admin import exchange_som
from create_bot import bot, dp 



@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.message):
    try:
        await bot.send_message(message.from_user.id, 'Приветсвую! Данный бот конвертируют вашу сумму в сомах на другие валюты')
        await message.delete()

    except:
        message.reply('Общение с ботом только через ЛС с @kaidu123')


@dp.message_handler(commands=['exchange'])
async def send_weater(message: types.message):
    text_part = message.text.split('/exchange ')
    if len(text_part) < 2:
        await message.reply("Пожайлуста напишите вашу сумму для конвертации рядом с коммандой weather пример: \'/exchange 5000'")
        return
    som = int(text_part[1])
    exchange_info = exchange_som(som)
    await message.reply(exchange_info)
    
async def on_startup(_):
    print('Бот вышел в онлайн')

