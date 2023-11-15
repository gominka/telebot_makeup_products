from telebot.types import CallbackQuery
from loguru import logger

import states
from database.models import Conditions
from handlers.custom_handlers import selection

from loader import bot
from user_interface import text


@bot.callback_query_handler(func=lambda call: call.data in ["user_search_brand", "user_search_tag",
                                                            "user_search_product_type", "user_search_name"])
def user_product_selection(call: CallbackQuery) -> None:
    """
    Обработчик callback-запросов, связанных с самостоятельным вводом данных пользователем

    :param call: callback-запросы
    :return: None
    """
    user_id = call.from_user.id
    chat_id = call.message.chat.id

    bot.send_message(chat_id=chat_id, text=text.USER_HANDLER)
    bot.set_state(user_id=user_id, state=states.custom_states.UserState.search_in_file, chat_id=chat_id)


@bot.callback_query_handler(func=lambda call: call.data in ["cancel"])
def user_product_selection(call: CallbackQuery) -> None:
    """
    Обработчик callback-запросов, связанных с самостоятельным вводом данных пользователем

    :param call: callback-запросы
    :return: None
    """
    bot.delete_message(call.message.chat.id, call.message.id)
    bot.delete_message(call.message.chat.id, call.message.id-1)


@bot.callback_query_handler(func=lambda call: call.data in ["deleting_adding"])
def commands_callback_main(call: CallbackQuery) -> None:
    """
    Обработчик callback-запроса, который удаляет последнюю занесенную информацию от пользователя

    :param call: callback-запрос удаления
    :return: None
    """
    Conditions.select().order_by(Conditions.id.desc()).get().delete_instance()
    logger.info(f'Удален последний запрос')
    bot.delete_message(call.message.chat.id, call.message.id)

# @bot.callback_query_handler(func=lambda call: call.data in ["type_search", "list_type"])
# def type_callback(call: CallbackQuery) -> None:
#     """
#     :param call: CallbackQuery
#     :return: None
#     """
#     if call.data == "type_search":
#         msg_brand = bot.send_message(call.message.chat.id, "Введите тип: ")  # ввести или выбрать
#         bot.register_next_step_handler(msg_brand, search_condition.set_type)
#     elif call.data == "list_type":
#         kb_types = keyboa_maker(items=product_types_handler(), copy_text_to_callback=True, items_in_row=3)
#         bot.send_message(
#             chat_id=call.message.chat.id, reply_markup=kb_types,
#             text="Please select one of the type:")
#
#
# @bot.callback_query_handler(func=lambda call: call.data in product_types_handler())
# def type_condition_search(call: CallbackQuery) -> None:
#     """
#
#       :param call:
#       :return: None
#     """
#     try:
#         user_id = call.from_user.id
#         cond = Conditions(product_type_cond=call.data,
#                           user_id=user_id)
#         cond.save()
#
#         bot.send_message(call.message.chat.id,
#                          "Выберете опцию: ", reply_markup=type_search_inline_btn())
#
#         logger.info(f'Выбран тип продукта. User_id: {user_id}, Type: {call.data}')
#     except IntegrityError:
#         # user_id = call.from_user.id
#         # cond = Conditions(product_type_cond=None, user_id=user_id)
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
#
#
# @bot.callback_query_handler(func=lambda call: call.data in ["typing"])
# def type_condition(call: CallbackQuery) -> None:
#     """
#     """
#     try:
#         cond = Conditions(product_type_cond=call.data, user_id=call.from_user.id).save()
#
#         if call.data == "typing":
#             bot.reply_to(message=call.message,
#                          text=dictionary['message']['brand'].format(
#                              emoji['highprice'],
#                              emoji['lowprice'],
#                              emoji['highrating'],
#                              emoji['lowrating'],
#                              emoji['custom'],
#                              emoji['tag'],
#                              emoji['product_type'],
#                              emoji['name'],
#                              emoji['add'],
#                              emoji['favourite']))
#
#     except IntegrityError:
#         bot.reply_to(message=call.message,
#                      text=dictionary['started_message']['help'].format(
#                          emoji['brand'],
#                          emoji['highprice'],
#                        emoji['lowprice'],
#                         emoji['highrating'],
#                           emoji['lowrating'],
#                          emoji['custom'],
#                          emoji['history'],
#                          emoji['favourite']))
