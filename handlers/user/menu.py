import asyncio

import aioschedule
import schedule
from aiogram.types import Message, CallbackQuery, ReplyKeyboardMarkup
from loader import dp, bot,db
from filters import IsAdmin, IsUser

catalog = '🍽Каталог'

cart = '🛒 Корзинка'
delivery_status = '🚚 Buyurtma holati'

settings = '⚙️Katalogni sozlash'
orders = '🚚 Buyurtmalar'
questions = '❓ Вопросы'
async def send_messange():
    fet=db.fetchall('SELECT * FROM cart WHERE cid=?')
    print(fet)
    await bot.send_message(chat_id=452785654,text='text')
@dp.message_handler(IsAdmin(), commands='start')
async def admin_menu(message: Message):
    markup = ReplyKeyboardMarkup(selective=True)
    markup.add(settings)
    markup.add(questions, orders)

    await message.answer('Menu', reply_markup=markup)

@dp.message_handler(IsUser(), commands='start')
async def user_menu(message: Message):
    fet=db.fetchall('SELECT cid FROM orders')
    a=len(fet)




    markup = ReplyKeyboardMarkup(selective=True)
    markup.add(catalog)
    markup.add(cart)

    await message.answer('Menu', reply_markup=markup)
    aioschedule.every().day.at("12:17").do(send_messange)
    aioschedule.every().day.at("12:18").do(send_messange)

    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)
