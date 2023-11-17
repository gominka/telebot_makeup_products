# from keyboa.keyboards import keyboa_maker
# from loguru import logger
# from peewee import IntegrityError
# from telebot.types import CallbackQuery
#
# from database.models import History
# from keyboards.inline.main_comm_inline_markup import search_inline_markup, web_inline_btn
# from loader import bot
# from site_ip.response_main import main_handler, brand_handler
#
#
# @bot.callback_query_handler(func=lambda call: call.data in ["list_brand"])
# def btn_list_condition(call: CallbackQuery) -> None:
#     """
#
#     :param call:
#     :return:
#     """
#     kb_brands = keyboa_maker(
#         items=brand_handler(),
#         copy_text_to_callback=True,
#         items_in_row=4
#     )
#     bot.send_message(
#         chat_id=call.message.chat.id,
#         reply_markup=kb_brands,
#         text="Выберете бренд"
#     )
#
#
# @bot.callback_query_handler(func=lambda call: call.data in brand_handler())
# def brand_condition_search(call: CallbackQuery) -> None:
#     """
#
#       :param call:
#       :return: None
#     """
#
#     try:
#         user_id = call.from_user.id
#         History(brand=call.data, user_id=user_id).save()
#
#         bot.send_message(call.message.chat.id,
#                          "Выберете опцию: ",
#                          reply_markup=search_inline_markup(call.message))
#
#         logger.info(f'Выбран бренд. User_id: {user_id}, Brand: {call.data}')
#
#     except IntegrityError:
#         # user_id = call.from_user.id
#         # Conditions(brand_cond=None, user_id=user_id)
#         # cond.save()
#         bot.reply_to(message=call.message,
#                      text="dddd")
#
#
#
#
