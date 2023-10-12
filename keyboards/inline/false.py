from telebot import types


def false_brand_markup():
    markup = types.InlineKeyboardMarkup(row_width=1)
    list_brand = types.InlineKeyboardButton(text='Вывести список всех имеющихся брендов',
                                            callback_data="list_brand")
    brand_search = types.InlineKeyboardButton(text='Попробовать еще раз',
                                              callback_data='brand_search')
    markup.add(list_brand, brand_search)
    return markup