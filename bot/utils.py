from aiogram.types import (
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)


LIST_KEYBOARD_BUTTONS_FOR_START_HANDLER = [
    [
        KeyboardButton(text="Web developer"),
        KeyboardButton(text="Python developer"),
    ],
    [       
        KeyboardButton(text="Javascript developer"),
        KeyboardButton(text="Data science developer"),
    ],
    [
        KeyboardButton(text="Golang developer"),
        KeyboardButton(text="Frontend developer"),
    ],
    [
        KeyboardButton(text="Backend developer"),
        KeyboardButton(text="Fullstack developer"),
    ]
]


JOB_POSITIONS = [
    "Web developer",
    "Python developer",
    "Javascript developer",
    "Data science",
    "Golang developer",
    "Frontend developer",
    "Backend developer",
    "Fullstack developer"
]


EXPERIENCE_LEVELS = [
    "No experience",
    "1 year",
    "1-2 years",
    "2-5 years",
    "5+"
]


def create_experience_keyboard(selected_experience=None):
    selected_experience = selected_experience or set()
    keyboard = InlineKeyboardMarkup()
    
    for experience in EXPERIENCE_LEVELS:
        label = f"{'✅ ' if experience in selected_experience else ''}{experience}"
        keyboard.add(InlineKeyboardButton(text=label, callback_data=f"experience:{experience}"))
    
    return keyboard