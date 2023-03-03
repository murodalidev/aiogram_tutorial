from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


productKeywords = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Kurslar', callback_data='courses'),
            InlineKeyboardButton(text='Kitoblar', callback_data='books'),
        ],
        [
            InlineKeyboardButton(text='GitHub sahifasiga o\'tish',
                                 url='https://github.com/murodalidev/aiogram-bot-template')
        ],
        [
            InlineKeyboardButton(text='Ulashish', switch_inline_query='Zor bot ekan')
        ]
    ]
)


coursesKeywords = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Python full stack', callback_data='python_courses'),
        ],
        [
            InlineKeyboardButton(text='Django courses', callback_data='django_courses'),
        ],
        [
            InlineKeyboardButton(text='Telegram bot courses', callback_data='tgbot_courses'),
        ],
        [
            InlineKeyboardButton(text='Ortga', callback_data='cancel'),
        ],
    ]
)


booksKeywords = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Python asoslari', callback_data='python_books'),
        ],
        [
            InlineKeyboardButton(text='JS asoslari', callback_data='js_books'),
        ],
        [
            InlineKeyboardButton(text='Django tutorial', callback_data='django_books'),
        ],
        [
            InlineKeyboardButton(text='Ortga', callback_data='cancel'),
        ],
    ]
)

soldKeyword = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='korish', url='https://github.com/murodalidev/aiogram-bot-template'),
        ],
    ]
)
