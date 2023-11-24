from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


def odin():
    """
    Формирование inline кнопок

    :param
    :return: markup
    """
    markup = InlineKeyboardMarkup(row_width=1)

    price = InlineKeyboardButton(text='Вывести цену', callback_data="price")
    rating = InlineKeyboardButton(text='Вывести рейтинг', callback_data="rating")
    api_featured_image = InlineKeyboardButton(text='Ссылка на картинку ', callback_data="api_featured_image")
    product_link = InlineKeyboardButton(text='Ссылка на продукт ', callback_data="product_link")
    description = InlineKeyboardButton(text='Вывести описание', callback_data="description")
    cancel = InlineKeyboardButton(text='Отмена', callback_data="cancel")

    markup.add(price, rating, api_featured_image, product_link, description, cancel)
    return markup
