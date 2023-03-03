import logging

from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp, bot
from aiogram.types import ReplyKeyboardRemove
from keyboards.inline.productKeywords import productKeywords, coursesKeywords, booksKeywords, soldKeyword


@dp.message_handler(text_contains="📚 Mahsulotlar")
async def select_category(msg: types.Message):
    await msg.answer("Mahsulotni tanlang:", reply_markup=productKeywords)


@dp.callback_query_handler(text='courses')
async def choose_course(call: types.CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.id=}")
    await call.message.edit_text('Kursni tanlang: ', reply_markup=coursesKeywords)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='books')
async def choose_books(call: types.CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.id=}")
    await call.message.edit_text('Kitobnini tanlang: ', reply_markup=booksKeywords)
    await call.answer(cache_time=60)


# course
@dp.callback_query_handler(text='tgbot_courses')
async def buying_course(call: types.CallbackQuery):
    await call.answer("Arizangiz qabul qilindi", cache_time=60, show_alert=True)
    await call.message.edit_text('Xodimimiz siz bilan boglanishini kuting', reply_markup=soldKeyword)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='python_courses')
async def buying_course(call: types.CallbackQuery):
    await call.answer("Arizangiz qabul qilindi", cache_time=60, show_alert=True)
    await call.message.edit_text('Xodimimiz siz bilan boglanishini kuting', reply_markup=soldKeyword)


@dp.callback_query_handler(text='django_courses')
async def buying_course(call: types.CallbackQuery):
    await call.answer("Arizangiz qabul qilindi", cache_time=60, show_alert=True)
    await call.message.edit_text('Xodimimiz siz bilan boglanishini kuting', reply_markup=soldKeyword)



# books
@dp.callback_query_handler(text='js_books')
async def buying_course(call: types.CallbackQuery):
    await call.answer("Arizangiz qabul qilindi", cache_time=60, show_alert=True)
    await call.message.edit_text('Xodimimiz siz bilan boglanishini kuting', reply_markup=soldKeyword)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text='python_books')
async def buying_course(call: types.CallbackQuery):
    await call.answer("Arizangiz qabul qilindi", cache_time=60, show_alert=True)
    await call.message.edit_text('Xodimimiz siz bilan boglanishini kuting', reply_markup=soldKeyword)


@dp.callback_query_handler(text='django_books')
async def buying_course(call: types.CallbackQuery):
    await call.answer("Arizangiz qabul qilindi", cache_time=60, show_alert=True)
    await call.message.edit_text('Xodimimiz siz bilan boglanishini kuting', reply_markup=soldKeyword)


# cancel
@dp.callback_query_handler(text='cancel')
async def cancel_menu(call: types.CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=productKeywords)
