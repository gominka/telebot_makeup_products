from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


def brand_inline_btn():
    """
    Формирование inline кнопок, при вызове команды /brand
    :param
    :return: markup
    """
    markup = InlineKeyboardMarkup(row_width=1)
    product_brand = InlineKeyboardButton(text='Поиск товара по бренду', #добавление бренда в условие поиска
                                         callback_data='product_brand')
    list_brand = InlineKeyboardButton(text='Вывести список всех брендов',
                                      callback_data="list_brand")
    brand_search = InlineKeyboardButton(text='Переход на сайт бренда',
                                        callback_data='brand_search')

    markup.add(list_brand, brand_search, product_brand)
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
