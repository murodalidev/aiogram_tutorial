import logging
import json
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.homeKeyboard import homeKey
from keyboards.default.registerKeyboard import registerKey
from loader import dp


@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: types.Message, state: FSMContext):
    logging.info(message)
    await state.finish()
    with open('users.json') as fp:
        users = json.load(fp)
    user = None
    for i in users:
        if i.get('telegram_id') == str(message.from_user.id):
            user = i
            break

    if user is not None:
        await message.answer(f"Assalomu Alaykum, {user.get('first_name')} {user.get('last_name')}.\nSiz ro'yhatdan o'tib bo'lgansiz.",
                             reply_markup=homeKey)
    else:
        await message.answer(f"Assalomu Alaykum, {message.from_user.full_name}!\nIltimos ro'yhatdan o'ting", reply_markup=registerKey)
