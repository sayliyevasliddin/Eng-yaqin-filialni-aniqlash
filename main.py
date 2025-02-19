from aiogram import Bot,Dispatcher,executor,types
from config import API_TOKEN
import logging
from buttons import eng_yaqin_filial
from functions import find_near_location
from aiogram.types import ReplyKeyboardRemove


logging.basicConfig(level=logging.INFO)


bot = Bot(API_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await message.answer(f"Salom {message.from_user.first_name}",reply_markup=eng_yaqin_filial)
    
@dp.message_handler(content_types=types.ContentType.LOCATION)
async def near_find_branchers(message: types.Message):
    location = message.location
    user_latitude = location.latitude
    user_longitude = location.longitude
    
    natija = await find_near_location(lat1=user_latitude, lon1=user_longitude)
    await message.answer(f"Eng yaqin filial: <b>{natija[0][0]}</b>.\nMasofa: <b>{natija[0][1]}</b> km.")
    await message.answer("Manzil: Qoratosh ko'chasi, 5A uy", reply_markup=ReplyKeyboardRemove())
    await message.answer_location(latitude=natija[0][2][0], longitude=natija[0][2][1])

    
    

    
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, reset_webhook=True)