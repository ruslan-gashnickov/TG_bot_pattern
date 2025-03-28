from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import  Command, CommandStart
from keyboards.keyboards import start_menu
from utils.logger import logger
router =  Router()



@router.message(CommandStart())
async def cmd_start(message: Message):
    logger.info(f"User started the bot. Admin:")
    welcome =(
        "Привет я бот построеный на шаблоне \n"
        "Это тестовое сообщение чтобы понять что работает команда старт"
    )

    await message.answer(welcome, reply_markup=start_menu())

@router.callback_query(F.data == "test_1")
async def cmd_test(messege: CallbackQuery):
    text = (

        "hi hi hi"
    )
    await messege.answer(text)

@router.message(F.text == "Привет")
async def text_hi(messege: Message):
    user = messege.from_user.full_name
    text = (f"Привет, {user}")
    await messege.reply(text)