"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging

from baza import Database

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text 
from buttons import *


API_TOKEN = '5892861686:AAGxT8VKvzFOK7BR8Ddc-8j9sGquGlIkFv4'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
db=Database()


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Assalomu aleykum\nQuyidagilaridan birini tanlang!",reply_markup=menu)

@dp.message_handler(text="Kitoblar")
async def send_welcome(message: types.Message):
    markup = await for_category_get_all()
    await message.reply("Bo'limlaridan birini tanlang!",reply_markup=markup)

@dp.callback_query_handler(Text(startswith="productall_"))
async def send_welcome(call: types.CallbackQuery):
    index = call.data.index('_')
    id = call.data[index+1:]
    products = await get_category_id(id)
    await call.message.reply("Kitoblardan birini tanlang!",reply_markup=products)

@dp.callback_query_handler(Text(startswith="products_"))
async def send_welcome(call: types.CallbackQuery):
    index = call.data.index('_')
    id = call.data[index+1:]
    product = db.select_product_id(id)
    await call.message.answer(f"Siz tanlangan kitob\nKitob nomi: {product[3]}\nKitob haqida: {product[4]}")





@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)