import os

from aiogram import types, Router, F
from aiogram.filters import CommandStart
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

from services.users_db import users_db
from keyboards import inline


user_private_router = Router()
ADMIN = os.getenv("ADMIN")

@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    if int(message.from_user.id) == int(ADMIN):
        await message.answer("WASSSSufrregp", reply_markup=inline.admin_buttons())
    else:
        await message.answer("WASSSSup", reply_markup=inline.categories_buttons())
    await users_db.add_user(message.from_user.id, message.from_user.first_name, message.from_user.last_name)


@user_private_router.message(F.text == "gay")
async def gay(message: types.Message):
    await message.reply("me too")