from telebot import types

from loader import bot

from site_ip.main_handler import make_response
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
