from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup



def failure_inline_markup(item):
    markup = InlineKeyboardMarkup(row_width=1)
    list = InlineKeyboardButton(text='Вывести список ',
                                callback_data="list_{}".format(item))
    search = InlineKeyboardButton(text='Попробовать еще раз',
                                  callback_data='user_search_{}'.format(item))
    markup.add(list, search)
    return markup



def search_inline_markup(item):
    """
    Формирование inline кнопок, при вызове команды /brand
    :param
    :return: markup
    """
    if item == "brand":
        markup = InlineKeyboardMarkup(row_width=1)
        list = InlineKeyboardButton(text='Поиск товаров по бренду',
                                    callback_data="branding")
        search = InlineKeyboardButton(text='Переход на сайт бренда',
                                      callback_data="web")
        cancel = InlineKeyboardButton(text='Отмена',
                                      callback_data='cancel_request')
        markup.add(list, search, cancel)
        return markup

    elif item == "tag":
        markup = InlineKeyboardMarkup(row_width=1)
        list = InlineKeyboardButton(text='Поиск товаров',
                                    callback_data="tagging")
        cancel = InlineKeyboardButton(text='Отмена',
                                      callback_data='cancel_request')
        markup.add(list, cancel)
        return markup
    elif item == "product_type":
        markup = InlineKeyboardMarkup(row_width=1)
        list = InlineKeyboardButton(text='Поиск товаров',
                                    callback_data="typing")
        cancel = InlineKeyboardButton(text='Отмена',
                                      callback_data='cancel_request')
        markup.add(list, cancel)
        return markup
