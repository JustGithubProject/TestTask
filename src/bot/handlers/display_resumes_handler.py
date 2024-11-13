from aiogram import (
    Router,
    F,
    types
)

from parser import filters
from parser.parser import get_resumes, request_to_site


display_resumes_router = Router()


@display_resumes_router.message(F.text == "1️⃣ Web developer")
async def handle_web_developer(message: types.Message):
    """Handler for the "Web developer" resume display"""
    
    url = filters.filter_by_job("Web developer")
    html_content = request_to_site(url)
    cards = get_resumes(html_content)
    
    for card in cards:
        await message.answer(
            f"{card['links']}"
        )


@display_resumes_router.message(F.text == "2️⃣ Python developer")
async def handle_python_developer(message: types.Message):
    """Handler for the "Python developer" resume display"""
    
    url = filters.filter_by_job("Python developer")
    html_content = request_to_site(url)
    cards = get_resumes(html_content)
    
    for card in cards:
        await message.answer(
            f"{card['links']}"
        )


@display_resumes_router.message(F.text == "3️⃣ Javascript developer")
async def handle_javascript_developer(message: types.Message):
    """Handler for the "Javascript developer" resume display"""
    
    url = filters.filter_by_job("Javascript developer")
    html_content = request_to_site(url)
    cards = get_resumes(html_content)
    
    for card in cards:
        await message.answer(
            f"{card['links']}"
        )


@display_resumes_router.message(F.text == "4️⃣ Data science developer")
async def handle_data_science_developer(message: types.Message):
    """Handler for the "Data science developer" resume display"""
    
    url = filters.filter_by_job("Data science developer")
    html_content = request_to_site(url)
    cards = get_resumes(html_content)
    
    for card in cards:
        await message.answer(
            f"{card['links']}"
        )
        

@display_resumes_router.message(F.text == "5️⃣ Golang developer")
async def handle_golang_developer(message: types.Message):
    """Handler for the "Golang developer" resume display"""
    
    url = filters.filter_by_job("Golang developer")
    html_content = request_to_site(url)
    cards = get_resumes(html_content)
    
    for card in cards:
        await message.answer(
            f"{card['links']}"
        )


@display_resumes_router.message(F.text == "6️⃣ Frontend developer")
async def handle_frontend_developer(message: types.Message):
    """Handler for the "Frontend developer" resume display"""
    
    url = filters.filter_by_job("Frontend developer")
    html_content = request_to_site(url)
    cards = get_resumes(html_content)
    
    for card in cards:
        await message.answer(
            f"{card['links']}"
        )


@display_resumes_router.message(F.text == "7️⃣ Backend developer")
async def handle_backend_developer(message: types.Message):
    """Handler for the "Backend developer" resume display"""
    
    url = filters.filter_by_job("Backend developer")
    html_content = request_to_site(url)
    cards = get_resumes(html_content)
    
    for card in cards:
        await message.answer(
            f"{card['links']}"
        )


@display_resumes_router.message(F.text == "8️⃣ Fullstack developer")
async def handle_fullstack_developer(message: types.Message):
    """Handler for the "Fullstack developer" resume display"""
    
    url = filters.filter_by_job("Fullstack developer")
    html_content = request_to_site(url)
    cards = get_resumes(html_content)
    
    for card in cards:
        await message.answer(
            f"{card['links']}"
        )