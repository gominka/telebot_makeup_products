# from loguru import logger
# from peewee import IntegrityError
# from telebot.types import CallbackQuery
#
# from database.models import History
# from keyboards.inline.main_comm_inline_markup import search_inline_markup
# from loader import bot
# from site_ip.main_handler import brands_list
#
#
#
# # @bot.callback_query_handler(func=lambda call: call.data in brands_list("brand"))
# # def call_btn_file(call: CallbackQuery) -> None:
# #     """
# #
# #       :param call:
# #       :return: None
# #     """
# #
# #     user_id = call.from_user.id
# #     chat_id = call.message.chat.id
# #     msg_user = call.data
# #
# #     try:
# #         with bot.retrieve_data(user_id=user_id, chat_id=chat_id) as data:
# #             data["params"]["brand"] = msg_user
# #
# #         if History.get_or_none(History.user_id == user_id) is None:
# #             History(brand=call.data.replace(' ', '%20'), user_id=user_id).save()
# #         else:
# #             History.update(brand=call.data.replace(' ', '%20')).where(History.user_id == user_id).execute()
# #
# #         logger.info(f'Выбран бренд. User_id: {user_id}, Brand: {msg_user}')
# #
# #         bot.send_message(
# #             chat_id=chat_id,
# #             text="Выберете опцию: ",
# #             reply_markup=search_inline_markup("brand")
# #         )
# #
# #     except IntegrityError:
# #         bot.reply_to(call.message, "Для начала поиска нажмите. Напишите /start")
#
#
# @bot.callback_query_handler(func=lambda call: call.data in params_handler("product_tag", params=BASE_PARAMS))
# def call_btn_file(call: CallbackQuery) -> None:
#     """
#
#       :param call:
#       :return: None
#     """
#
#     user_id = call.from_user.id
#     chat_id = call.message.chat.id
#     msg_user = call.data
#
#     try:
#         with bot.retrieve_data(user_id=user_id, chat_id=chat_id) as data:
#             data["params"]["product_tag"] = msg_user.replace(' ', '%20')
#
#         if History.get_or_none(History.user_id == user_id) is None:
#             History(tag=call.data.replace(' ', '%20'), user_id=user_id).save()
#         else:
#             History.update(tag=call.data.replace(' ', '%20')).where(History.user_id == user_id).execute()
#
#         logger.info(f'Выбран тэг. User_id: {user_id}, Tag: {call.data}')
#
#         bot.send_message(
#             chat_id=chat_id,
#             text="Выберете опцию: ",
#             reply_markup=search_inline_markup("tag")
#         )
#
#     except IntegrityError:
#         bot.reply_to(call.message, "Для начала поиска нажмите. Напишите /start")
#
#
# @bot.callback_query_handler(func=lambda call: call.data in params_handler("product_type", params=BASE_PARAMS))
# def call_btn_file(call: CallbackQuery) -> None:
#     """
#
#       :param call:
#       :return: None
#     """
#
#     user_id = call.from_user.id
#     chat_id = call.message.chat.id
#     msg_user = call.data
#
#     try:
#         with bot.retrieve_data(user_id=user_id, chat_id=chat_id) as data:
#             data["params"]["product_type"] = msg_user.replace(' ', '%20')
#
#         if History.get_or_none(History.user_id == user_id) is None:
#             History(product_type=msg_user, user_id=user_id).save()
#         else:
#             History.update(product_type=msg_user).where(History.user_id == user_id).execute()
#
#         logger.info(f'Выбран product_type. User_id: {user_id}, Product_type: {call.data}')
#
#         bot.send_message(
#             chat_id=chat_id,
#             text="Выберете опцию: ",
#             reply_markup=search_inline_markup("product_type")
#         )
#
#     except IntegrityError:
#         bot.reply_to(call.message, "Для начала поиска нажмите. Напишите /start")
