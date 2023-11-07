from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


def type_inline_btn():
    """
    Формирование inline кнопок, при вызове команды /brand
    :param
    :return: markup
    """
    markup = InlineKeyboardMarkup(row_width=1)
    product_type = InlineKeyboardButton(text='Поиск товаров по бренду',
                                        callback_data='product_type')
    list_type = InlineKeyboardButton(text='Вывести список всех типов',
                                     callback_data="list_type")

    markup.add(list_type, product_type)
    return markup


def type_search_inline_btn():
    """
    Формирование inline кнопок, при вызове команды /brand
    :param
    :return: markup
    """
    markup = InlineKeyboardMarkup(row_width=1)
    list_types = InlineKeyboardButton(text='Поиск товаров по типу',
                                      callback_data="typing")
    cancel_type = InlineKeyboardButton(text='Отмена',
                                       callback_data='cancel_type')
    markup.add(list_types, cancel_type)
    return markup
