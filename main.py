import asyncio

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.client.default import DefaultBotProperties

from config import config
from utils.logger import logger
from handiers import common
async def main():
# Инициализация бота и диспетчера - исправленная версия
    bot = Bot(
        token=config.BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp = Dispatcher()


    dp.include_router(common.router)

    logger.info("Starting bot...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("Bot stopped!")