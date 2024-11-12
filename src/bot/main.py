import asyncio

from aiogram import (
    Bot,
    Dispatcher,
)
from aiogram.enums import ParseMode

from config import TOKEN

from handlers.base_handler import base_router


async def main():
    bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher()

    dp.include_router(base_router)

    await dp.start_polling(bot)


asyncio.run(main())