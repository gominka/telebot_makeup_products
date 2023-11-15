# from loguru import logger
#
# from database.models import Conditions
# from handlers.custom_handlers.check import check_cond_in_file
# from keyboards.inline.main_comm_inline_markup import false_brand_inline_markup, search_brand_inline_btn
# from loader import bot
#
#
# def user_select_brand(message) -> None:
#     user_brand = message.text.lower()
#     if check_cond_in_file("brand", user_brand):
#         Conditions(brand_cond=user_brand,
#                    user_id=message.from_user.id).save()
#         logger.info('Выбранное условие: ' + user_brand + f' User_id - {message.from_user.id}')
#
#         bot.send_message(message.chat.id,
#                          "Выберете опцию: ",
#                          reply_markup=search_brand_inline_btn())
#
#     else:
#         bot.send_message(message.chat.id,
#                          text="Не можем найти такой бренд. ",
#                          reply_markup=false_brand_inline_markup())
#
#
# def user_select_tag(message) -> None:
#     user_tag = message.text.lower()
#     if check_cond_in_file("tag", user_tag):
#         Conditions(tag_cond=user_tag, user_id=message.from_user.id).save()
#         logger.info('Выбранное условие: ' + user_tag + f' User_id - {message.from_user.id}')
#
#         bot.send_message(message.chat.id,
#                          "Выберете опцию: ",
#                          reply_markup=search_brand_inline_btn())
#
#     else:
#         bot.send_message(message.chat.id,
#                          text="Не можем найти такой бренд. ",
#                          reply_markup=false_brand_inline_markup())
#
#
# def user_select_product_type(message) -> None:
#
#     # TODO: разобраться с регистром
#     user_type = message.text.lower()
#     if check_cond_in_file("product_type", user_type):
#         Conditions(brand_cond=user_type,
#                    user_id=message.from_user.id).save()
#         logger.info('Выбранное условие: ' + user_type + f' User_id - {message.from_user.id}')
#
#         bot.send_message(message.chat.id,
#                          "Выберете опцию: ",
#                          reply_markup=search_brand_inline_btn())
#
#     else:
#         bot.send_message(message.chat.id,
#                          text="Не можем найти такой бренд. ",
#                          reply_markup=false_brand_inline_markup())
