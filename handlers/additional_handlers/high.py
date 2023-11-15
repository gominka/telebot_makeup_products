from telebot.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

from loader import bot


cond1 = ""
cond2 = ""


@bot.message_handler(commands=['high', 'low', 'custom'])
def low_high_handler(message: Message) -> None:
    """
    Обработчик каманд: /high, /low, /custom
    Запрашивается условие

    :param message: выбранная команда
    :return None
    """

    global cond1
    cond1 = message
    markup = InlineKeyboardMarkup(row_width=1)
    price = InlineKeyboardButton(text='Поиск по цене',
                                 callback_data="price")
    rating = InlineKeyboardButton(text='Поиск по рейтингу',
                                  callback_data='rating')
    cancel = InlineKeyboardButton(text='Узнать топ товаров по заданному диапазону',
                                  callback_data='Отмена')
    markup.add(price, rating, cancel)
    bot.send_message(message.chat.id, 'Выберите условие поиска:',
                     reply_markup=markup)
#
#
# @bot.message_handler(content_types=['text'])
# def txt(message: types.Message):
#     if message.text == "Бренд":
#         brand.brand(message)
#     elif message.text == "Тэг":
#         tag.tag(message)
#     elif message.text == "Тип продукта":
#         product_type.product_type(message)
#
# @bot.message_handler(state=UserState.condition_selection)
# def select_condition(call: CallbackQuery) -> None:
#     global cond1
#     global cond2
#     cond2 = call.message.text
#     print(cond2)
#     if cond1 == "/low":
#         max_value = bot.send_message(call.message.chat.id, "Выберите максимальное значение: ")
#         bot.register_next_step_handler(max_value, find)
#     elif cond1 == "/high":
#         min_value = bot.send_message(call.message.chat.id, "Выберите минимальное значение: ")
#         bot.register_next_step_handler(min_value, find)
#     elif cond1 == "/custom":
#         max_value = bot.send_message(call.message.chat.id, "Выберите диапазон значение: ")
#         bot.register_next_step_handler(max_value, find)
#
#
# def find(message: Message):
#     value = [cond1, cond2, message.text]
#     print(value)
#     bot.send_message(message.chat.id, "Идёт поиск: ")
