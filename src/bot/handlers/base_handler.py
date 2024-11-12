from aiogram import Router

from handlers.start_handler import start_router
from handlers.display_resumes_handler import  display_resumes_router


base_router = Router()

base_router.include_routers(
    start_router,
    display_resumes_router
)