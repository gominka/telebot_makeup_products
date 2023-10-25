#
# from handlers.additional_handlers import brand, product_type, tag
# from loader import bot
#
# from telebot import types
#
#
#
# @bot.callback_query_handler(func=lambda call: call.data == [call.data == "type_search", "typing_search",
#                                                             "list_type", "sec_type", "name"])
# def answer(call: types.CallbackQuery) -> None:
#     if call.data == "type_search":
#         msg_type = bot.send_message(call.message.chat.id, "Введите тип: ")
#         bot.register_next_step_handler(msg_type, product_type.set_type)
#     elif call.data == "list_type":
#         with open('product_type.txt', 'r') as f:
#             a = [line.strip() for line in f]
#             bot.send_message(call.message.chat.id,
#                              '\n'.join(map(str, sorted(a))))
#     elif call.data == "sec_type":
#         product_type.product_type(call.message)
#     elif call.data == "branding_search":
#         msg_type = bot.send_message(call.message.chat.id, "Введите тип: ")
#         bot.register_next_step_handler(msg_type, product_type.set_type)
#     elif call.data == "name":
#         pass
#
#
