from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import  Command, CommandStart
from keyboards.keyboards import start_menu

router =  Router()



@router.message(CommandStart())
async def cmd_start(message: Message):
    welcome =(
        "Привет я бот построеный на шаблоне \n"
        "Это тестовое сообщение чтобы понять что работает команда старт"
    )

    await message.answer(welcome, reply_markup=start_menu())