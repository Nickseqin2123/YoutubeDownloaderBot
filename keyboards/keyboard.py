from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def menu():
    butt = [
        [KeyboardButton(text="Скачать видео с YouTube")],
        [KeyboardButton(text="Скачать песню из VK")]
    ]

    button_maker = ReplyKeyboardMarkup(keyboard=butt,
                                       resize_keyboard=True)

    return button_maker


def button_for():
    button_maker = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Главное меню")]],
                                       resize_keyboard=True,
                                       input_field_placeholder="Введи ссылку (пожалуйста)")
    return button_maker