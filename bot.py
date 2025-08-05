from aiogram import Bot, Dispatcher, types
from aiogram.types import WebAppInfo, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor

# Твой Telegram Bot Token
TOKEN = "7926988231:AAGlqZNcBm-q3hd5KHBdHMOn-H5_-xwet5w"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("🪳 Играть", web_app=WebAppInfo(url="https://tarakan-game-2.onrender.com")))
    await message.answer("Нажми кнопку ниже, чтобы начать игру:", reply_markup=markup)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
