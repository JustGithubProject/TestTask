from aiogram import Router, types
from aiogram.types import ReplyKeyboardMarkup
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

import utils


start_router = Router()

@start_router.message(Command(commands="start"))
async def send_welcome(message: types.Message, state: FSMContext):
    await message.answer(
        "👋 Привіт! Обери потрібний тобі варіант!",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=utils.LIST_KEYBOARD_BUTTONS_FOR_START_HANDLER,
            resize_keyboard=True
        )
    )