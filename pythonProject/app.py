import asyncio
import os
import logging

from aiogram import Bot, Dispatcher, types

from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

from handlers.user_private import user_private_router
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


bot = Bot(token=os.getenv("TOKEN"))
dp = Dispatcher()
dp.include_router(user_private_router)

async def main():
    await dp.start_polling(bot)

asyncio.run(main())