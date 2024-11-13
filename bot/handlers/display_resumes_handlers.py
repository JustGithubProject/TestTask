from aiogram import (
    Router,
    F,
    types
)

from parser import filters
from parser.parser import get_resumes, request_to_site


display_resumes_router = Router()


@display_resumes_router.message(F.text == "Web developer")
async def handle_web_developer(message: types.Message):
    """Handler for the "Web developer" resume display"""
    
    url = filters.filter_by_job(message.text)
    html_content = request_to_site(url)
    cards = get_resumes(html_content)
    
    for card in cards:
        await message.answer(
            f"{card['links']}"
        )


@display_resumes_router.message(F.text == "Python developer")
async def handle_python_developer(message: types.Message):
    """Handler for the "Python developer" resume display"""
    
    url = filters.filter_by_job(message.text)
    html_content = request_to_site(url)
    cards = get_resumes(html_content)
    
    for card in cards:
        await message.answer(
            f"{card['links']}"
        )


@display_resumes_router.message(F.text == "Javascript developer")
async def handle_javascript_developer(message: types.Message):
    """Handler for the "Javascript developer" resume display"""
    
    url = filters.filter_by_job(message.text)
    html_content = request_to_site(url)
    cards = get_resumes(html_content)
    
    for card in cards:
        await message.answer(
            f"{card['links']}"
        )


@display_resumes_router.message(F.text == "Data science developer")
async def handle_data_science_developer(message: types.Message):
    """Handler for the "Data science developer" resume display"""
    
    url = filters.filter_by_job(message.text)
    html_content = request_to_site(url)
    cards = get_resumes(html_content)
    
    for card in cards:
        await message.answer(
            f"{card['links']}"
        )
        

@display_resumes_router.message(F.text == "Golang developer")
async def handle_golang_developer(message: types.Message):
    """Handler for the "Golang developer" resume display"""
    
    url = filters.filter_by_job(message.text)
    html_content = request_to_site(url)
    cards = get_resumes(html_content)
    
    for card in cards:
        await message.answer(
            f"{card['links']}"
        )


@display_resumes_router.message(F.text == "Frontend developer")
async def handle_frontend_developer(message: types.Message):
    """Handler for the "Frontend developer" resume display"""
    
    url = filters.filter_by_job(message.text)
    html_content = request_to_site(url)
    cards = get_resumes(html_content)
    
    for card in cards:
        await message.answer(
            f"{card['links']}"
        )


@display_resumes_router.message(F.text == "Backend developer")
async def handle_backend_developer(message: types.Message):
    """Handler for the "Backend developer" resume display"""
    
    url = filters.filter_by_job(message.text)
    html_content = request_to_site(url)
    cards = get_resumes(html_content)
    
    for card in cards:
        await message.answer(
            f"{card['links']}"
        )


@display_resumes_router.message(F.text == "Fullstack developer")
async def handle_fullstack_developer(message: types.Message):
    """Handler for the "Fullstack developer" resume display"""
    
    url = filters.filter_by_job(message.text)
    html_content = request_to_site(url)
    cards = get_resumes(html_content)
    
    for card in cards:
        await message.answer(
            f"{card['links']}"
        )