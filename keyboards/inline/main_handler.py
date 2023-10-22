from telebot import types


def command_type_markup():
    markup = types.InlineKeyboardMarkup(row_width=1)
    list_type = types.InlineKeyboardButton(text='Вывести список типов продуктов',
                                           callback_data="list_type")
    type_search = types.InlineKeyboardButton(text='Поиск по типу',
                                             callback_data='type_search')
    markup.add(list_type, type_search)
    return markup


def command_tag_markup():
    markup = types.InlineKeyboardMarkup(row_width=1)
    list_tag = types.InlineKeyboardButton(text='Вывести список всех тэгов',
                                          callback_data="list_tag")
    tag_search = types.InlineKeyboardButton(text='Поиск по tag',
                                            callback_data='tag_search')
    markup.add(list_tag, tag_search)
    return markup
