from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

homeKey = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🔙 Orqaga qaytish'),
            KeyboardButton(text="📚 Mahsulotlar"),
        ]
    ],
    resize_keyboard=True
)