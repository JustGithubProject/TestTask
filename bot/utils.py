from aiogram.types import (
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)


LIST_KEYBOARD_BUTTONS_FOR_START_HANDLER = [
    [
        KeyboardButton(text="work.ua"),
        KeyboardButton(text="robota.ua")
    ]
]


LIST_KEYBOARD_BUTTONS_FOR_JOB_POSITION_HANDLER = [
    [
        KeyboardButton(text="Cancel")
    ],
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
    ],

]


LIST_KEYBOARD_BUTTONS_FOR_LOCATION_HANDLER = [
    [
        KeyboardButton(text="Cancel")
    ],
    [
        KeyboardButton(text="Вся Україна"),
        KeyboardButton(text="Київ"),
        KeyboardButton(text="Житомир"),
        KeyboardButton(text="Львів"),
    ],
    [
        KeyboardButton(text="Одеса"),
        KeyboardButton(text="Дніпро"),
        KeyboardButton(text="Вінниця"),
        KeyboardButton(text="Полтава"),
    ],
    [
        KeyboardButton(text="Чернігів"),
        KeyboardButton(text="Черкаси"),
        KeyboardButton(text="Суми"),
        KeyboardButton(text="Миколаїв"),
    ],
    [
        KeyboardButton(text="Херсон"),
        KeyboardButton(text="Рівне"),
        KeyboardButton(text="Хмельницький"),
        KeyboardButton(text="Тернопіль"),
    ],
    [
        KeyboardButton(text="Івано-Франківськ"),
        KeyboardButton(text="Луцьк"),
        KeyboardButton(text="Ужгород"),
        KeyboardButton(text="Харків"),

    ]
]

LIST_KEYBOARD_BUTTONS_FOR_EXPERIENCE_HANDLER = [
    [
        KeyboardButton(text="Без досвіду"),
        KeyboardButton(text="Cancel")
    ],
    [
        KeyboardButton(text="1 рік"),
        KeyboardButton(text="1-2 роки"),
        KeyboardButton(text="2-5 роки"),
        KeyboardButton(text="5+ років"),
    ]
]


LIST_KEYBOARD_BUTTONS_FOR_SALARY_HANDLER = [
    [
        KeyboardButton(text="до 10 000 грн"),
        KeyboardButton(text="до 15 000 грн"),
        KeyboardButton(text="до 20 000 грн"),
        KeyboardButton(text="до 30 000 грн")
    ],
    [
        KeyboardButton(text="до 40 000 грн"),
        KeyboardButton(text="до 50 000 грн"),
        KeyboardButton(text="до 100 000 грн"),
        KeyboardButton(text="Cancel")
    ]
]


JOB_POSITIONS = [
    "Web developer",
    "Python developer",
    "Javascript developer",
    "Data science developer",
    "Golang developer",
    "Frontend developer",
    "Backend developer",
    "Fullstack developer"
]


EXPERIENCE_LEVELS = [
    "Без досвіду",
    "1 рік",
    "1-2 роки",
    "2-5 роки",
    "5+ років"
]


