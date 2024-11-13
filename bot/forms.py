from aiogram.fsm.state import State, StatesGroup


class ResumeFilterForm(StatesGroup):
    location = State()
    experience = State()
    salary = State()
