# from telebot import types
#
# from loader import bot
# import datetime
# from keyboa import Keyboa
#
# from telebot import types
#
# from loader import bot
# from states.custom_states import UserState
#
# cond1 = ''
# cond2 = ''
#
#
# @bot.message_handler(commands=['high', 'low', 'custom'])
# def low_high_handler(message: types.Message) -> None:
#     """
#     Обработчик каманд: /high, /low, /custom
#     Запрашиваем условие поиска.
#     :param message: Message
#     :return None
#     """
#     global cond1
#     cond1 = message.text
#     markup = [["Поиск по цене", "Поиск по рейтингу"], ["Отмена"]]
#     kb = Keyboa(markup).keyboard
#     bot.set_state(message.from_user.id, state=UserState.condition_selection)
#     bot.send_message(chat_id=message.chat.id, text='Выберите условие поиска:',
#                      reply_markup=kb)
#
#
# @bot.message_handler(state=UserState.condition_selection)
# def select_condition(message: types.Message) -> None:
#     global cond1
#     global cond2
#     cond2 = message.text
#     if cond1 == "/low":
#         max_value = bot.send_message(message.chat.id, "Выберите максимальное значение: ")
#         bot.register_next_step_handler(max_value, find)
#     elif cond1 == "/high":
#         min_value = bot.send_message(message.chat.id, "Выберите минимальное значение: ")
#         bot.register_next_step_handler(min_value, find)
#     elif cond1 == "/custom":
#         max_value = bot.send_message(message.chat.id, "Выберите диапазон значение: ")
#         bot.register_next_step_handler(max_value, find)
#
#
# def find(message: types.Message):
#     value = [cond1, cond2, message.text]
#     print(value)
#     bot.send_message(message.chat.id, "Идёт поиск: ")
