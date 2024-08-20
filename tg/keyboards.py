from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv


load_dotenv()


main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='reg')],
    ],
    resize_keyboard=True
)
