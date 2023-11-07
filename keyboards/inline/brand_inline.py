from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


def main_commands_inline_btn(item):
    """
    Формирование inline кнопок, при вызове основных команд
    :param
    :return: markup
    """

    markup = InlineKeyboardMarkup(row_width=1)
    user_selection = InlineKeyboardButton(text='Ввести самостоятельно',
                                          callback_data='product_{}'.format(item))
    system_selection = InlineKeyboardButton(text='Выбрать из представленных',
                                            callback_data='list_{}'.format(item))
    markup.add(user_selection, system_selection)
    return markup


def search_brand_inline_btn():
    """
    Формирование inline кнопок, при вызове команды /brand
    :param
    :return: markup
    """

    markup = InlineKeyboardMarkup(row_width=1)
    list_brand = InlineKeyboardButton(text='Поиск товаров по бренду',
                                      callback_data="branding")
    brand_search = InlineKeyboardButton(text='Переход на сайт бренда',
                                        callback_data="web")
    cancel_brand = InlineKeyboardButton(text='Отмена',
                                        callback_data='cancel_brand')
    markup.add(list_brand, brand_search, cancel_brand)
    return markup


def false_brand_inline_btn():
    markup = InlineKeyboardMarkup(row_width=1)
    list_brand = InlineKeyboardButton(text='Вывести список брендов',
                                      callback_data="list_brand")
    brand_search = InlineKeyboardButton(text='Попробовать еще раз',
                                        callback_data='brand_search')
    markup.add(list_brand, brand_search)
    return markup


def web_inline_btn(fl):
    markup = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton("Перейти на сайт",
                                   url=fl[0]['website_link'])
    markup.add(button1)
    return markup
