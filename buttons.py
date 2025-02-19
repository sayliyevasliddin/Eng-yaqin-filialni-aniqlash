from aiogram.types import KeyboardButton,ReplyKeyboardMarkup


eng_yaqin_filial = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("Eng yqin filialni aniqlash", request_location=True)]
    ],
    resize_keyboard=True, 
    one_time_keyboard=True
)