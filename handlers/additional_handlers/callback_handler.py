from loguru import logger
from telebot import types
from telebot.types import CallbackQuery

from handlers.default_handlers.exception_handler import exc_handler

from loader import bot
from site_ip.main_handler import conditions_list, make_response
from user_interface import text


@bot.callback_query_handler(func=lambda call: call.data in ["check_len_responce"])
def check_in_site_call(call: types.CallbackQuery) -> None:

    user_id = call.from_user.id
    chat_id = call.message.chat.id

    with bot.retrieve_data(user_id=user_id, chat_id=chat_id) as data:
        params = data["params"]

    if len(make_response(params=params)) == 1:

        with bot.retrieve_data(user_id=user_id, chat_id=chat_id) as data:
            data["id"] = make_response(params=params)[0]["id"]

        markup = types.InlineKeyboardMarkup(row_width=1)
        description = types.InlineKeyboardButton(text='Вывести описание', callback_data="description")
        image = types.InlineKeyboardButton(text='Показать картинку', callback_data="image")
        product_link = types.InlineKeyboardButton(text='Ссылка на продукт ', callback_data="product_link")

        cancel = types.InlineKeyboardButton(text='Отмена', callback_data="cancel")

        markup.add(description, image, product_link, cancel)

        bot.send_message(chat_id=chat_id, text="Выберите, что хотите сделать", reply_markup=markup)

    elif 1 <= len(make_response(params=params)) <= 5:

        markup = types.InlineKeyboardMarkup(row_width=3)
        name = types.InlineKeyboardButton(text='Вывести названия', callback_data="list_name_product")
        cancel = types.InlineKeyboardButton(text='Отмена', callback_data="cancel")

        markup.add(name,  cancel)

        with bot.retrieve_data(user_id=user_id, chat_id=chat_id) as data:
            data["cond"] = "name_products"

        bot.send_message(chat_id=chat_id, text="Выберите, что хотите сделать", reply_markup=markup)

    else:
        bot.send_message(chat_id=call.message.chat.id, text=text.CONDITION)

@bot.callback_query_handler(func=lambda call: call.data in ["check_len_responce"])
@exc_handler
def call_btn_file(call: CallbackQuery) -> None:

    user_id = call.from_user.id
    chat_id = call.message.chat.id

    with bot.retrieve_data(user_id=user_id, chat_id=chat_id) as data:
        params = data["params"]

    bot.send_message(chat_id=chat_id, text=str(conditions_list(params=params, selected_condition=call.data)))




    markup = types.InlineKeyboardMarkup(row_width=1)
    custom_search = types.InlineKeyboardButton(text='Продолжить поиск', callback_data="check_len_responce")
    favourite = types.InlineKeyboardButton(text='Добавить в избранное', callback_data="favourite")
    cancel = types.InlineKeyboardButton(text='Отмена', callback_data='cancel_request')
    markup.add(custom_search, favourite)

    if cond == "brand":
        website = types.InlineKeyboardButton(text='Переход на сайт бренда', callback_data="website_link")
        markup.add(website)

