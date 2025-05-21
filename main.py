import os
import sys
import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from dotenv import load_dotenv
from bot.handlers.main import start, foods, food, recipe_of_food

load_dotenv()

token = os.getenv('BOT_TOKEN')


async def main():
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)

    bot = Bot(token=token)
    dp = Dispatcher(bot=bot)

    dp.message.register(start, Command(commands='start'))
    dp.callback_query.register(foods, F.data.startswith('foods'))
    dp.callback_query.register(food, F.data.startswith('food'))
    dp.callback_query.register(recipe_of_food, F.data.startswith('recipe_of_'))


    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(main())
