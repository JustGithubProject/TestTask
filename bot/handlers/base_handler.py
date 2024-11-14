from aiogram import Router

from handlers.start_handler import start_router
from handlers.work_ua_handlers.display_resumes_handlers import work_ua_display_resumes_router


base_router = Router()

base_router.include_routers(
    start_router,
    work_ua_display_resumes_router
)