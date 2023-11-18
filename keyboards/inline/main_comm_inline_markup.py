from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


def main_commands_inline_markup(item):
    """
    Формирование inline кнопок, при вызове команд /brand, /tag и /type

    :param
    :return: markup
    """

    markup = InlineKeyboardMarkup(row_width=1)
    user_selection = InlineKeyboardButton(text='Ввести самостоятельно',
                                          callback_data='user_search_{}'.format(item))
    system_selection = InlineKeyboardButton(text='Выбрать из представленных',
                                            callback_data='list_{}'.format(item))
    cancel = InlineKeyboardButton(text='Отмена', callback_data="cancel")
    markup.add(user_selection, system_selection, cancel)
    return markup


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


def web_inline_btn(fl):
    markup = InlineKeyboardMarkup()
    web_btn = InlineKeyboardButton("Перейти на сайт",
                                   url=fl[0]['website_link'])
    markup.add(web_btn)
    return markup
