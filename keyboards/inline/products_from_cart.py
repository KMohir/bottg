from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

product_cb = CallbackData('product', 'id', 'action')

def product_markup(idx, count):

    global product_cb

    markup = InlineKeyboardMarkup()
    back_btn = InlineKeyboardButton('⬅️', callback_data=product_cb.new(id=idx, action='decrease'))
    count_btn = InlineKeyboardButton(count, callback_data=product_cb.new(id=idx, action='count'))
    next_btn = InlineKeyboardButton('➡️', callback_data=product_cb.new(id=idx, action='increase'))
    delete = InlineKeyboardButton('🚫 Отмена заказа', callback_data=product_cb.new(id=idx, action='delete'))
    markup.row(back_btn, count_btn, next_btn)
    markup.add(delete)

    return markup




