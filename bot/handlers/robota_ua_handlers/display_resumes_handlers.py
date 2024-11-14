import time
import asyncio

from aiogram import (
    Router,
    F,
    types
)

from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardMarkup

from robota_ua_parser.parser import (
    get_resumes,
    request_to_site
)

from robota_ua_parser.filters import (
    filter_by_job,
    filter_by_location,
    filter_by_experience,
    filter_by_salary
)

from forms import ResumeRobotaUAFilterForm
from utils import (
    LIST_KEYBOARD_BUTTONS_FOR_JOB_POSITION_HANDLER,
    LIST_KEYBOARD_BUTTONS_FOR_LOCATION_HANDLER,
    LIST_KEYBOARD_BUTTONS_FOR_EXPERIENCE_HANDLER,
    LIST_KEYBOARD_BUTTONS_FOR_SALARY_HANDLER
)

robota_ua_display_resumes_router = Router()



@robota_ua_display_resumes_router.message(F.text == "robota.ua")
async def handle_robota_ua(message: types.Message, state: FSMContext):
    # await state.update_data(site=message.text)
    await state.set_state(ResumeRobotaUAFilterForm.site)
    await message.answer(
        "Обери потрібний тобі варіант!",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=LIST_KEYBOARD_BUTTONS_FOR_JOB_POSITION_HANDLER,
            resize_keyboard=True
        )
    )
    
    
@robota_ua_display_resumes_router.message(ResumeRobotaUAFilterForm.site)
async def process_site(message: types.Message, state: FSMContext):
    job_position = filter_by_job(message.text)
    await state.update_data(job_position=job_position)
    await state.set_state(ResumeRobotaUAFilterForm.location)
    await message.answer(
        "Виберіть місто для пошуку",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=LIST_KEYBOARD_BUTTONS_FOR_LOCATION_HANDLER,
            resize_keyboard=True
        )
    )


@robota_ua_display_resumes_router.message(ResumeRobotaUAFilterForm.location)
async def process_location(message: types.Message, state: FSMContext):
    location = filter_by_location(message.text)
    await state.update_data(location=location)
    await state.set_state(ResumeRobotaUAFilterForm.experience)
    await message.answer(
       "Виберіть бажаний досвід кандидата",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=LIST_KEYBOARD_BUTTONS_FOR_EXPERIENCE_HANDLER,
            resize_keyboard=True
        )
    )
    
    
@robota_ua_display_resumes_router.message(ResumeRobotaUAFilterForm.experience)
async def process_experience(message: types.Message, state: FSMContext):
    experience = filter_by_experience(message.text)
    await state.update_data(experience=experience)
    await state.set_state(ResumeRobotaUAFilterForm.salary)
    await message.answer(
        "Виберіть діапазон заробітної плати",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=LIST_KEYBOARD_BUTTONS_FOR_SALARY_HANDLER,
            resize_keyboard=True
        )
    )

@robota_ua_display_resumes_router.message(ResumeRobotaUAFilterForm.salary)
async def process_salary(message: types.Message, state: FSMContext):
    salary = filter_by_salary(message.text)
    await state.update_data(salary=salary)
    data = await state.get_data()
    current_url = data["job_position"]
    current_url = current_url.replace("ukraine", data["location"])
    current_url += data["experience"]
    current_url += data["salary"]
    print(current_url)
    html_content, driver = request_to_site(current_url)
    await asyncio.sleep(3)
    resumes = get_resumes(html_content)
    if not resumes:
        driver.quit()
        await message.answer("Кандидатів за вказаними параметрами не знайдено.")
    else:
        driver.quit()        
        for resume in resumes:
            await message.answer(resume) 