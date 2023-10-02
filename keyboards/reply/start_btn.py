from telebot import types


def btn_start(message: types.Message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    btn_brand = types.KeyboardButton(text='Бренд')
    btn_tag = types.KeyboardButton(text='Тэг')
    btn_type = types.KeyboardButton(text='Тип продукта')
    markup.add(btn_brand, btn_tag, btn_type)
    return markup
