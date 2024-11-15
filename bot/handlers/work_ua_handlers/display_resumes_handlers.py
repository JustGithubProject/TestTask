from aiogram import (
    Router,
    F,
    types
)
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardMarkup


from work_ua_parser import filters
from work_ua_parser.parser import get_resumes, request_to_site
from forms import ResumeWorkUAFilterForm

from utils import (
    JOB_POSITIONS,
    LIST_KEYBOARD_BUTTONS_FOR_LOCATION_HANDLER,
    LIST_KEYBOARD_BUTTONS_FOR_EXPERIENCE_HANDLER,
    LIST_KEYBOARD_BUTTONS_FOR_SALARY_HANDLER,
    LIST_KEYBOARD_BUTTONS_FOR_JOB_POSITION_HANDLER,
    LIST_KEYBOARD_BUTTONS_FOR_START_HANDLER
)


work_ua_display_resumes_router = Router()


@work_ua_display_resumes_router.message(F.text == "Cancel")
async def cancel_handler(message: types.Message, state: FSMContext):
    """
        Cancels the current process and clears the state,
        then prompts the user to select an action from the main menu.
    """
    await state.clear()
    await message.answer(
        "Обери потрібний тобі варіант!",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=LIST_KEYBOARD_BUTTONS_FOR_START_HANDLER,
            resize_keyboard=True
        )
    )
    

@work_ua_display_resumes_router.message(F.text == "work.ua")
async def handle_work_ua(message: types.Message, state: FSMContext):
    """
        Initializes the resume search process
        by prompting the user to select a job position.
    """
    await state.set_state(ResumeWorkUAFilterForm.site)
    await message.answer(
        "Обери потрібний тобі варіант!",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=LIST_KEYBOARD_BUTTONS_FOR_JOB_POSITION_HANDLER,
            resize_keyboard=True
        )
    )


@work_ua_display_resumes_router.message(ResumeWorkUAFilterForm.site)
async def handle_job_position(message: types.Message, state: FSMContext):
    """
        Processes the selected job position,
        updates the search URL, and prompts the user to choose a location.
    """
    
    current_url = filters.filter_by_job(message.text)
    await state.update_data(current_url=current_url)
    await state.set_state(ResumeWorkUAFilterForm.location)
    await message.answer(
        "Виберіть місто для пошуку",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=LIST_KEYBOARD_BUTTONS_FOR_LOCATION_HANDLER,
            resize_keyboard=True
        )
    )



@work_ua_display_resumes_router.message(ResumeWorkUAFilterForm.location)
async def process_location(message: types.Message, state: FSMContext):
    """
        Processes the selected location, updates the search URL
        with the location, and asks the user to choose
        the desired experience level.
    """
    
    # Converting a location to part of a URL path
    location = filters.filter_by_location(message.text)
    data = await state.get_data()
    current_url = data["current_url"]
    print("Location", current_url)
    current_url += location
    await state.update_data(current_url=current_url)
    print(current_url)
    
    await state.set_state(ResumeWorkUAFilterForm.experience)
    await message.answer(
        "Виберіть бажаний досвід кандидата",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=LIST_KEYBOARD_BUTTONS_FOR_EXPERIENCE_HANDLER,
            resize_keyboard=True
        )
    )


@work_ua_display_resumes_router.message(ResumeWorkUAFilterForm.experience)
async def process_experience(message: types.Message, state: FSMContext):
    """
        Processes the selected experience level, updates the search URL,
        and asks the user to choose a salary range.
    """
    
    # Converting an experience to part of a URL path
    experience = filters.filter_by_experience(message.text)
    data = await state.get_data()
    current_url = data["current_url"]
    print("Experience", current_url)
    current_url += experience
    await state.update_data(current_url=current_url)
    await state.set_state(ResumeWorkUAFilterForm.salary)
    
    await message.answer(
        "Виберіть діапазон заробітної плати",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=LIST_KEYBOARD_BUTTONS_FOR_SALARY_HANDLER,
            resize_keyboard=True
        )
    )


@work_ua_display_resumes_router.message(ResumeWorkUAFilterForm.salary)
async def process_salary(message: types.Message, state: FSMContext):
    """
        Processes the selected salary range, updates the search URL,
        fetches the data, and displays the resumes or informs the user if no results were found.
    """
    
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
        
   
        

