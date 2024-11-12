from aiogram import (
    Router,
    F,
    types
)

from parser import filters
from parser.main import get_resumes, request_to_site


display_resumes_router = Router()


@display_resumes_router.message(F.text == "1️⃣ Web developer")
async def handle_web_developer(message: types.Message):
    url = filters.filter_by_job("Web developer")
    html_content = request_to_site(url)
    cards = get_resumes(html_content)
    
    for card in cards:
        await message.answer(
            f"{card['links']}"
        )


@display_resumes_router.message(F.text == "2️⃣ Python developer")
async def handle_python_developer(message: types.Message):
    url = filters.filter_by_job("Python developer")
    html_content = request_to_site(url)
    cards = get_resumes(html_content)
    
    for card in cards:
        await message.answer(
            f"{card['links']}"
        )


@display_resumes_router.message(F.text == "3️⃣ Javascript developer")
async def handle_javascript_developer(message: types.Message):
    url = filters.filter_by_job("Javascript developer")
    html_content = request_to_site(url)
    cards = get_resumes(html_content)
    
    for card in cards:
        await message.answer(
            f"{card['links']}"
        )  