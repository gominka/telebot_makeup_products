# import datetime
#
# from telebot import types, logger
# from telebot.types import Message
#
# from loader import bot
# from states.state import UserInputState
#
#
# @bot.message_handler(commands=['high', 'low', 'custom'])
# def low_high_handler(message: types.Message) -> None:
#     """
#     Обработчик каманд: /high, /low
#     Запрашиваем условие поиска.
#     :param message: types.Message
#     :return None
#     """
#     bot.set_state(message.chat.id, UserInputState.command)
#     bot.set_state(message.chat.id, UserInputState.condition_selection)
#     markup = types.InlineKeyboardMarkup(row_width=1)
#     price = types.InlineKeyboardButton(text='Поиск по цене',
#                                        callback_data="price")
#     rating = types.InlineKeyboardButton(text='Поиск по рейтингу',
#                                         callback_data='rating')
#     markup.add(price, rating)
#     bot.send_message(message.chat.id, 'Выберите условие поиска:',
#                      reply_markup=markup)
#     print(message.text)
#     with bot.retrieve_data(message.chat.id) as data:
#         data['condition'] = message.text
#         logger.info('Выбранное условие' + message.text + f'User_id {message.chat.id}')
#         # Cоздание запроса
#
#
# @bot.callback_query_handler(func=lambda call: call.data == ['price', 'rating'])
# def callback_min_price(call: types.CallbackQuery):
#     min_value = bot.send_message(call.message.chat.id, "Выберите минимальное значение: ")
#     bot.register_next_step_handler(min_value, find_price)
#
#
# @bot.message_handler(state=UserInputState.condition_selection)
# def select_condition(message: types.Message) -> None:
#     """
#     Обработчик каманд: /high, /low
#     Запрашиваем условие поиска.
#     :param message: types.Message
#     :return None
#     """
#     with bot.retrieve_data(message.chat.id) as data:
#         data['condition'] = message.text
#         logger.info('Выбранное условие' + message.text + f'User_id {message.chat.id}')
#         # Cоздание запроса
#
#     bot.set_state(message.chat.id, UserInputState.condition_selection)
#     markup = types.InlineKeyboardMarkup(row_width=1)
#     price = types.InlineKeyboardButton(text='Поиск по цене',
#                                        callback_data="price")
#     rating = types.InlineKeyboardButton(text='Поиск по рейтингу',
#                                         callback_data='rating')
#     markup.add(price, rating)
#     bot.send_message(message.chat.id, 'Выберите условие поиска:',
#                      reply_markup=markup)
#     with bot.retrieve_data(message.chat.id) as data:
#         data.clear()
#         logger.info('Выбранное условие' + message.text + f'User_id {message.chat.id}')
#         data['condition'] = message.text
#         data['data_time'] = datetime.datetime.now().strftime('%d.%m.%y %h:%m:%s')
#         data['chat_id'] = message.chat.id
#
#
# @bot.callback_query_handler(func=lambda call: call.data == 'min_price')
# def callback_min_price(call: types.CallbackQuery):
#     min_value = bot.send_message(call.message.chat.id, "Выберите минимальное значение: ")
#     bot.register_next_step_handler(min_value, find_price)
#
#
# @bot.callback_query_handler(func=lambda call: call.data == 'min_price')
# def callback_min_rating(call: types.CallbackQuery):
#     min_value = bot.send_message(call.message.chat.id, "Выберите минимальное значение: ")
#     bot.register_next_step_handler(min_value, find_rat)
#
#
# @bot.callback_query_handler(func=lambda call: call.data == 'max_price')
# def callback_max(call: types.CallbackQuery):
#     max_value = bot.send_message(call.message.chat.id, "Выберите максимальное значение: ")
#     bot.register_next_step_handler(max_value, find_price)
#
#
# @bot.callback_query_handler(func=lambda call: call.data == 'max_rating')
# def callback_max(call: types.CallbackQuery):
#     max_value = bot.send_message(call.message.chat.id, "Выберите максимальное значение: ")
#     bot.register_next_step_handler(max_value, find_rat)
#
#
# def find_price(message: types.Message):
#     bot.send_message(message.chat.id, "Идёт поиск: ")
#
#
# def find_rat(message: types.Message):
#     bot.send_message(message.chat.id, "Идёт поиск: ")
#
#
# @bot.message_handler(commands=['custom'])
# def custom(message: types.Message) -> None:
#     markup = types.InlineKeyboardMarkup(row_width=1)
#     price = types.InlineKeyboardButton(text='Поиск по цене',
#                                        callback_data="price")
#     rating = types.InlineKeyboardButton(text='Поиск по рейтингу',
#                                         callback_data='rating')
#     markup.add(price, rating)
#     bot.send_message(message.chat.id, 'Выберите условие поиска:',
#                      reply_markup=markup)
