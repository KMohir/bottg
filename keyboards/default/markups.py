from aiogram.types import ReplyKeyboardMarkup
back_message = '👈 Назад'
confirm_message = '✅ Подтверждение заказа'
all_right_message = "✅ Все правильно"
cancel_message = '🚫 Отмена'
catalog = '🍽Каталог'
cart = '🛒 Корзинка'
def confirm_markup():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.add(confirm_message)
    markup.add(back_message)

    return markup

def back_markup():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.add(back_message)

    return markup

def check_markup():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.row(back_message, all_right_message)

    return markup

def submit_markup():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.row(cancel_message, all_right_message)

    return markup

def yangiz():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.row(catalog)

    markup.row(cart)
    return markup

