from aiogram.fsm.state import State, StatesGroup


class ResumeWorkUAFilterForm(StatesGroup):
    site = State()
    location = State()
    experience = State()
    salary = State()


class ResumeRobotaUAFilterForm(StatesGroup):
    site = State()
    location = State()
    experience = State()
    salary = State()