from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton, ReplyKeyboardMarkup,KeyboardButton


#Кнопки для теста
def start_menu():
    buttons = [
        [InlineKeyboardButton(text="Кнопка 1", callback_data="test_1")],
        [InlineKeyboardButton(text="Кнопка 2", callback_data="test_2")]
    ]

    return InlineKeyboardMarkup(inline_keyboard=buttons)