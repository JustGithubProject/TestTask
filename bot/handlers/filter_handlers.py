from aiogram import (
    Router,
    F,
    types
)

from utils import JOB_POSITIONS


filter_router = Router()


@filter_router.message(F.text in JOB_POSITIONS)
async def select_experience(message: types.Message):
    pass