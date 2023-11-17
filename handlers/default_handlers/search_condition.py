# from peewee import IntegrityError
# from loguru import logger
#
# from telebot.types import Message
#
# from database.models import User
# from keyboards.inline.main_comm_inline_markup import main_commands_inline_markup
# from keyboards.reply.reply_keyboards import get_reply_keyboard
# from user_interface import text
# from loader import bot
# import states.custom_states
# from user_interface.emoji import emoji
#
#
# @bot.message_handler(commands=['brand', 'tag', 'product_type', 'name'])
# def search_state(message: Message) -> None:
#     msg_user = message.text[1:]
#     user_id = message.from_user.id
#     chat_id = message.chat.id
#
#     if User.get_or_none(User.user_id == user_id) is None:
#         bot.reply_to(message, "Вы не зарегистрированы. Напишите /start")
#         return
#
#     with bot.retrieve_data(user_id=user_id, chat_id=chat_id) as data:
#         data["first_cond"] = msg_user
#
#     bot.send_message(chat_id=chat_id,
#                      text="Выберете условие для продолжения поиска: ",
#                      reply_markup=main_commands_inline_markup(msg_user)
#                      )
#
#
# # def set_brand(message: Message) -> None:
# #     user_brand = message.text.lower()
# #     if check_brand(user_brand):
# #         fl = list(filter(lambda x: x['brand'] == user_brand, main_handler()))
# #
# #         bot.send_message(message.chat.id,
# #                          "Для перехода на сайт нажмите на кнопку".format(message.from_user),
# #                          reply_markup=web_inline_btn(fl))
# #
# #     else:
# #         bot.send_message(message.chat.id,
# #                          text="Не можем найти такой бренд. ",
# #                          reply_markup=false_brand_inline_btn())
#
# # @bot.callback_query_handler(func=lambda call: call.data in ["brand_search",
# #                                                             "list_brand",
# #
# #                                                             "branding",
# #                                                             "web"])
# # def brand_callback_main(call: CallbackQuery) -> None:
# #     """
# #     Обработчик callback-запросов, предназначенный для  поиском и работы с "Брендами"
# #
# #     :param call: callback-запрос.
# #     :return: None
# #     """
# #
# #     #
# #     if call.data == "brand_search":
# #         # TODO: ввести или выбрать
# #         pass
# #
# #
# #
# #     # вывод всех брендов кнопками
# #     elif call.data == "list_brand":
# #         kb_brands = keyboa_maker(items=brand_handler(),
# #                                  copy_text_to_callback=True,
# #                                  items_in_row=4)
# #         bot.send_message(
# #             chat_id=call.message.chat.id, reply_markup=kb_brands,
# #             text="Выберете бренд")
# #
# #     # Поиск товаров по бренду
# #     elif call.data == "branding":
# #         bot.reply_to(message=call.message,
# #                      text=dictionary['message']['brand'].format(
# #                          emoji['highprice'],
# #                          emoji['lowprice'],
# #                          emoji['highrating'],
# #                          emoji['lowrating'],
# #                          emoji['custom'],
# #                          emoji['tag'],
# #                          emoji['product_type'],
# #                          emoji['name'],
# #                          emoji['add'],
# #                          emoji['favourite']))
# #
# #
# #     # переход на сайт бренда
# #     elif call.data == "web":
# #         try:
# #             sql_select = str(
# #                 Conditions.select(Conditions.brand_cond).where(Conditions.user_id == call.from_user.id).get())
# #             fl = list(filter(lambda x: x['brand'] == sql_select, main_handler()))
# #             bot.send_message(call.message.chat.id,
# #                              "Для перехода на сайт нажмите на кнопку".format(call.message.from_user),
# #                              reply_markup=web_inline_btn(fl))
# #
# #         except TypeError:
# #             bot.send_message(call.message.chat.id, "Ошибка")
# #
# #
# # @bot.callback_query_handler(func=lambda call: call.data in ["type_search", "list_type"])
# # def type_callback(call: CallbackQuery) -> None:
# #     """
# #     :param call: CallbackQuery
# #     :return: None
# #     """
# #     if call.data == "type_search":
# #         msg_brand = bot.send_message(call.message.chat.id, "Введите тип: ")  # ввести или выбрать
# #         bot.register_next_step_handler(msg_brand, search_condition.set_type)
# #     elif call.data == "list_type":
# #         kb_types = keyboa_maker(items=product_types_handler(), copy_text_to_callback=True, items_in_row=3)
# #         bot.send_message(
# #             chat_id=call.message.chat.id, reply_markup=kb_types,
# #             text="Please select one of the type:")
# #
# #
# # @bot.callback_query_handler(func=lambda call: call.data in product_types_handler())
# # def type_condition_search(call: CallbackQuery) -> None:
# #     """
# #
# #       :param call:
# #       :return: None
# #     """
# #     try:
# #         user_id = call.from_user.id
# #         cond = Conditions(product_type_cond=call.data,
# #                           user_id=user_id)
# #         cond.save()
# #
# #         bot.send_message(call.message.chat.id,
# #                          "Выберете опцию: ", reply_markup=type_search_inline_btn())
# #
# #         logger.info(f'Выбран тип продукта. User_id: {user_id}, Type: {call.data}')
# #     except IntegrityError:
# #         # user_id = call.from_user.id
# #         # cond = Conditions(product_type_cond=None, user_id=user_id)
# #         # cond.save()
# #         bot.reply_to(message=call.message,
# #                      text=dictionary['started_message']['help'].format(
# #                          emoji['brand'],
# #                          emoji['highprice'],
# #                          emoji['lowprice'],
# #                          emoji['highrating'],
# #                          emoji['lowrating'],
# #                          emoji['custom'],
# #                          emoji['history'],
# #                          emoji['favourite']))
# #
# #
# # @bot.callback_query_handler(func=lambda call: call.data in ["typing"])
# # def type_condition(call: CallbackQuery) -> None:
# #     """
# #     """
# #     try:
# #         cond = Conditions(product_type_cond=call.data, user_id=call.from_user.id).save()
# #
# #         if call.data == "typing":
# #             bot.reply_to(message=call.message,
# #                          text=dictionary['message']['brand'].format(
# #                              emoji['highprice'],
# #                              emoji['lowprice'],
# #                              emoji['highrating'],
# #                              emoji['lowrating'],
# #                              emoji['custom'],
# #                              emoji['tag'],
# #                              emoji['product_type'],
# #                              emoji['name'],
# #                              emoji['add'],
# #                              emoji['favourite']))
# #
# #     except IntegrityError:
# #         bot.reply_to(message=call.message,
# #                      text=dictionary['started_message']['help'].format(
# #                          emoji['brand'],
# #                          emoji['highprice'],
# #                        emoji['lowprice'],
# #                         emoji['highrating'],
# #                           emoji['lowrating'],
# #                          emoji['custom'],
# #                          emoji['history'],
# #                          emoji['favourite']))
#
# #
#
# # def set_brand(message: Message) -> None:
# #     user_brand = message.text.lower()
# #     if check_brand(user_brand):
# #         fl = list(filter(lambda x: x['brand'] == user_brand, main_handler()))
# #
# #         bot.send_message(message.chat.id,
# #                          "Для перехода на сайт нажмите на кнопку".format(message.from_user),
# #                          reply_markup=web_inline_btn(fl))
# #
# #     else:
# #         bot.send_message(message.chat.id,
# #                          text="Не можем найти такой бренд. ",
# #                          reply_markup=false_brand_inline_btn())
# #
# #
