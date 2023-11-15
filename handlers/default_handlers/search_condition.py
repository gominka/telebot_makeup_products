# from keyboa.keyboards import keyboa_maker
# from loguru import logger
# from peewee import IntegrityError
# from telebot.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
#
# from database.models import User, Conditions
# import handlers.callback_handlers
# from handlers.dictionary import emoji, dictionary
# from keyboards.inline.brand_inline import (
#     false_brand_inline_btn,
#     web_inline_btn,
#     main_commands_inline_btn, search_brand_inline_btn
# )
# from keyboards.inline.types_inline import type_search_inline_btn
# from loader import bot
# from site_ip.response_main import main_handler, product_types_handler, brand_handler
#
#

#
# #
# def set_brand(message: Message) -> None:
#     user_brand = message.text.lower()
#     if check_brand(user_brand):
#         fl = list(filter(lambda x: x['brand'] == user_brand, main_handler()))
#
#         bot.send_message(message.chat.id,
#                          "Для перехода на сайт нажмите на кнопку".format(message.from_user),
#                          reply_markup=web_inline_btn(fl))
#
#     else:
#         bot.send_message(message.chat.id,
#                          text="Не можем найти такой бренд. ",
#                          reply_markup=false_brand_inline_btn())
from telebot.types import Message

from database.models import User
import handlers.callback_handlers
from keyboards.inline.main_comm_inline_markup import (
    main_commands_inline_markup
)
from loader import bot
from states.custom_states import UserState

# @bot.callback_query_handler(func=lambda call: call.data in ["brand_search",
#                                                             "list_brand",
#
#                                                             "branding",
#                                                             "web"])
# def brand_callback_main(call: CallbackQuery) -> None:
#     """
#     Обработчик callback-запросов, предназначенный для  поиском и работы с "Брендами"
#
#     :param call: callback-запрос.
#     :return: None
#     """
#
#     #
#     if call.data == "brand_search":
#         # TODO: ввести или выбрать
#         pass
#
#
#
#     # вывод всех брендов кнопками
#     elif call.data == "list_brand":
#         kb_brands = keyboa_maker(items=brand_handler(),
#                                  copy_text_to_callback=True,
#                                  items_in_row=4)
#         bot.send_message(
#             chat_id=call.message.chat.id, reply_markup=kb_brands,
#             text="Выберете бренд")
#
#     # Поиск товаров по бренду
#     elif call.data == "branding":
#         bot.reply_to(message=call.message,
#                      text=dictionary['message']['brand'].format(
#                          emoji['highprice'],
#                          emoji['lowprice'],
#                          emoji['highrating'],
#                          emoji['lowrating'],
#                          emoji['custom'],
#                          emoji['tag'],
#                          emoji['product_type'],
#                          emoji['name'],
#                          emoji['add'],
#                          emoji['favourite']))
#
#
#     # переход на сайт бренда
#     elif call.data == "web":
#         try:
#             sql_select = str(
#                 Conditions.select(Conditions.brand_cond).where(Conditions.user_id == call.from_user.id).get())
#             fl = list(filter(lambda x: x['brand'] == sql_select, main_handler()))
#             bot.send_message(call.message.chat.id,
#                              "Для перехода на сайт нажмите на кнопку".format(call.message.from_user),
#                              reply_markup=web_inline_btn(fl))
#
#         except TypeError:
#             bot.send_message(call.message.chat.id, "Ошибка")
#
#
# @bot.callback_query_handler(func=lambda call: call.data in brand_handler())
# def brand_condition_search(call: CallbackQuery) -> None:
#     """
#       :param call:
#       :return: None
#     """
#
#     try:
#         user_id = call.from_user.id
#         Conditions(brand_cond=call.data, user_id=user_id).save()
#
#         bot.send_message(call.message.chat.id,
#                          "Выберете опцию: ",
#                          reply_markup=search_brand_inline_btn())
#
#         logger.info(f'Выбран бренд. User_id: {user_id}, Brand: {call.data}')
#
#     except IntegrityError:
#         # user_id = call.from_user.id
#         # Conditions(brand_cond=None, user_id=user_id)
#         # cond.save()
#         bot.reply_to(message=call.message,
#                      text=dictionary['started_message']['help'].format(
#                          emoji['brand'],
#                          emoji['highprice'],
#                          emoji['lowprice'],
#                          emoji['highrating'],
#                          emoji['lowrating'],
#                          emoji['custom'],
#                          emoji['history'],
#                          emoji['favourite']))


# def set_brand(message: Message) -> None:
#     user_brand = message.text.lower()
#     if check_brand(user_brand):
#         fl = list(filter(lambda x: x['brand'] == user_brand, main_handler()))
#
#         bot.send_message(message.chat.id,
#                          "Для перехода на сайт нажмите на кнопку".format(message.from_user),
#                          reply_markup=web_inline_btn(fl))
#
#     else:
#         bot.send_message(message.chat.id,
#                          text="Не можем найти такой бренд. ",
#                          reply_markup=false_brand_inline_btn())
#
#
