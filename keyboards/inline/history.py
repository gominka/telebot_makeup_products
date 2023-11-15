from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


def inline_btn_history():
    markup = InlineKeyboardMarkup(row_width=1)
    brands = InlineKeyboardButton(text='Вывести историю поиска брендов',
                                  callback_data="brands_history")
    types = InlineKeyboardButton(text='Вывести историю поиска типов',
                                 callback_data="types_history")
    tags = InlineKeyboardButton(text='Вывести историю поиска тэгов',
                                callback_data="tags_history")
    products = InlineKeyboardButton(text='Вывести историю поиска продуктов',
                                    callback_data="products_history")
    all_history = InlineKeyboardButton(text='Вывести историю поиска',
                                       callback_data="all_history")

    markup.add(brands, types, tags, products, all_history)

    return markup
