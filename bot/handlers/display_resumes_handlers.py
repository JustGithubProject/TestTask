from aiogram import (
    Router,
    F,
    types
)
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardMarkup


from work_ua_parser import filters
from work_ua_parser.parser import get_resumes, request_to_site
from forms import ResumeFilterForm

from utils import (
    LIST_KEYBOARD_BUTTONS_FOR_LOCATION_HANDLER,
    LIST_KEYBOARD_BUTTONS_FOR_EXPERIENCE_HANDLER,
    LIST_KEYBOARD_BUTTONS_FOR_SALARY_HANDLER,
    LIST_KEYBOARD_BUTTONS_FOR_JOB_POSITION_HANDLER
)


display_resumes_router = Router()


@display_resumes_router.message(F.text == "Cancel")
async def cancel_handler(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer(
        "Обери потрібний тобі варіант!",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=LIST_KEYBOARD_BUTTONS_FOR_JOB_POSITION_HANDLER,
            resize_keyboard=True
        )
    )
    


@display_resumes_router.message(F.text == "Web developer")
async def handle_web_developer(message: types.Message, state: FSMContext):
    """Handler for the "Web developer" resume display"""
    
    current_url = filters.filter_by_job(message.text)
    print(current_url)
    await state.update_data(current_url=current_url)
    await state.set_state(ResumeFilterForm.location)
    await message.answer(
        "Виберіть місто для пошуку",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=LIST_KEYBOARD_BUTTONS_FOR_LOCATION_HANDLER,
            resize_keyboard=True
        )
    )
    # html_content = request_to_site(url)
    # cards = get_resumes(html_content)
    
    # for card in cards:
    #     await message.answer(
    #         f"{card['links']}"
    #     )


@display_resumes_router.message(F.text == "Python developer")
async def handle_python_developer(message: types.Message, state: FSMContext):
    """Handler for the "Python developer" resume display"""
    current_url = filters.filter_by_job(message.text)
    print(current_url)
    await state.update_data(current_url=current_url)
    await state.set_state(ResumeFilterForm.location)
    await message.answer(
        "Виберіть місто для пошуку",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=LIST_KEYBOARD_BUTTONS_FOR_LOCATION_HANDLER,
            resize_keyboard=True
        )
    )
    # html_content = request_to_site(url)
    # cards = get_resumes(html_content)
    
    # for card in cards:
    #     await message.answer(
    #         f"{card['links']}"
    #     )


@display_resumes_router.message(F.text == "Javascript developer")
async def handle_javascript_developer(message: types.Message, state: FSMContext):
    """Handler for the "Javascript developer" resume display"""
    current_url = filters.filter_by_job(message.text)
    print(current_url)
    await state.update_data(current_url=current_url)
    await state.set_state(ResumeFilterForm.location)
    await message.answer(
        "Виберіть місто для пошуку",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=LIST_KEYBOARD_BUTTONS_FOR_LOCATION_HANDLER,
            resize_keyboard=True
        )
    )
    # html_content = request_to_site(url)
    # cards = get_resumes(html_content)
    
    # for card in cards:
    #     await message.answer(
    #         f"{card['links']}"
    #     )


@display_resumes_router.message(F.text == "Data science developer")
async def handle_data_science_developer(message: types.Message, state: FSMContext):
    """Handler for the "Data science developer" resume display"""
    current_url = filters.filter_by_job(message.text)
    print(current_url)
    await state.update_data(current_url=current_url)
    await state.set_state(ResumeFilterForm.location)
    await message.answer(
        "Виберіть місто для пошуку",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=LIST_KEYBOARD_BUTTONS_FOR_LOCATION_HANDLER,
            resize_keyboard=True
        )
    )
    # html_content = request_to_site(url)
    # cards = get_resumes(html_content)
    
    # for card in cards:
    #     await message.answer(
    #         f"{card['links']}"
    #     )
        

@display_resumes_router.message(F.text == "Golang developer")
async def handle_golang_developer(message: types.Message, state: FSMContext):
    """Handler for the "Golang developer" resume display""" 
    current_url = filters.filter_by_job(message.text)
    print(current_url)
    await state.update_data(current_url=current_url)
    await state.set_state(ResumeFilterForm.location)
    await message.answer(
        "Виберіть місто для пошуку",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=LIST_KEYBOARD_BUTTONS_FOR_LOCATION_HANDLER,
            resize_keyboard=True
        )
    )
    # html_content = request_to_site(url)
    # cards = get_resumes(html_content)
    
    # for card in cards:
    #     await message.answer(
    #         f"{card['links']}"
    #     )


@display_resumes_router.message(F.text == "Frontend developer")
async def handle_frontend_developer(message: types.Message, state: FSMContext):
    """Handler for the "Frontend developer" resume display"""
    current_url = filters.filter_by_job(message.text)
    print(current_url)
    await state.update_data(current_url=current_url)
    await state.set_state(ResumeFilterForm.location)
    await message.answer(
        "Виберіть місто для пошуку",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=LIST_KEYBOARD_BUTTONS_FOR_LOCATION_HANDLER,
            resize_keyboard=True
        )
    )
    # html_content = request_to_site(url)
    # cards = get_resumes(html_content)
    
    # for card in cards:
    #     await message.answer(
    #         f"{card['links']}"
    #     )


@display_resumes_router.message(F.text == "Backend developer")
async def handle_backend_developer(message: types.Message, state: FSMContext):
    """Handler for the "Backend developer" resume display"""
    current_url = filters.filter_by_job(message.text)
    print(current_url)
    await state.update_data(current_url=current_url)
    await state.set_state(ResumeFilterForm.location)
    await message.answer(
        "Виберіть місто для пошуку",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=LIST_KEYBOARD_BUTTONS_FOR_LOCATION_HANDLER,
            resize_keyboard=True
        )
    )
    # html_content = request_to_site(url)
    # cards = get_resumes(html_content)
    
    # for card in cards:
    #     await message.answer(
    #         f"{card['links']}"
    #     )


@display_resumes_router.message(F.text == "Fullstack developer")
async def handle_fullstack_developer(message: types.Message, state: FSMContext):
    """Handler for the "Fullstack developer" resume display"""
    current_url = filters.filter_by_job(message.text)
    print(current_url)
    await state.update_data(current_url=current_url)
    await state.set_state(ResumeFilterForm.location)
    await message.answer(
        "Виберіть місто для пошуку кандидата",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=LIST_KEYBOARD_BUTTONS_FOR_LOCATION_HANDLER,
            resize_keyboard=True
        )
    )
    # html_content = request_to_site(url)
    # cards = get_resumes(html_content)
    
    # for card in cards:
    #     await message.answer(
    #         f"{card['links']}"
    #     )


@display_resumes_router.message(ResumeFilterForm.location)
async def process_location(message: types.Message, state: FSMContext):
    
    # Converting a location to part of a URL path
    location = filters.filter_by_location(message.text)
    data = await state.get_data()
    current_url = data["current_url"]
    print("Location", current_url)
    current_url += location
    await state.update_data(current_url=current_url)
    print(current_url)
    
    await state.set_state(ResumeFilterForm.experience)
    await message.answer(
        "Виберіть бажаний досвід кандидата",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=LIST_KEYBOARD_BUTTONS_FOR_EXPERIENCE_HANDLER,
            resize_keyboard=True
        )
    )


@display_resumes_router.message(ResumeFilterForm.experience)
async def process_experience(message: types.Message, state: FSMContext):
    
    # Converting an experience to part of a URL path
    experience = filters.filter_by_experience(message.text)
    data = await state.get_data()
    current_url = data["current_url"]
    print("Experience", current_url)
    current_url += experience
    await state.update_data(current_url=current_url)
    await state.set_state(ResumeFilterForm.salary)
    
    await message.answer(
        "Виберіть діапазон заробітної плати",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=LIST_KEYBOARD_BUTTONS_FOR_SALARY_HANDLER,
            resize_keyboard=True
        )
    )


@display_resumes_router.message(ResumeFilterForm.salary)
async def process_salary(message: types.Message, state: FSMContext):
    
    # Convert salary to part of a URL path
    salary = filters.filter_by_salary(message.text)
    data = await state.get_data()
    current_url = data["current_url"]
    print("Salary", current_url)
    current_url += salary
    print(current_url)
    await state.update_data(current_url=current_url)
    
    try:
        print(current_url)
        html_content = request_to_site(current_url)
            
        # Process the resumes
        cards = get_resumes(html_content)
        print(cards)
        if cards:
            for card in cards:
                await message.answer(
                    f"{card['links']}"
                )
        else:
            await message.answer("Кандидатів за вказаними параметрами не знайдено.")
                
    except Exception as e:
        print(f"Error: {e}")
        await message.answer("На жаль, не вдалося знайти потрібних кандидатів.")
        await state.clear()
        
   
        

