

import os
import logging
import openai
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

api_token_telegram = '6005245198:AAFHo6pfzJYap_fUP8fQlJII4k-WZ_jdoPo'
open_ai_api_key = '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'

# Инициализация бота и диспетчера
bot = Bot(token=api_token_telegram)
dp = Dispatcher(bot)

# Инициализация API ключа OpenAI
openai.api_key = open_ai_api_key

# Логирование
logging.basicConfig(level=logging.INFO)

# Обработка команды /start
@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Привет! Я ChatGPT бот. Я могу ответить на твои вопросы.")

# Обработка текстовых сообщений
@dp.message_handler(content_types=["text"])
async def echo_message(message: types.Message):
    question = message.text
    answer = openai.Completion.create(
        engine="davinci",
        prompt=question,
        temperature=0.7,
        max_tokens=1024,
        n=1,
        stop=None,
        timeout=10,
    )
    await message.reply(answer.choices[0].text)

# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
