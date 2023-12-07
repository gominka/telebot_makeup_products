from loguru import logger
from telebot import types

import states
from database.models import Favorite
from handlers.default_handlers.exception_handler import exc_handler
from loader import bot
from site_ip.main_handler import make_response
from user_interface import text


@bot.callback_query_handler(func=lambda call: call.data in ["check_amount_products"])
def check_amount_products(call: types.CallbackQuery) -> None:

    user_id = call.from_user.id
    chat_id = call.message.chat.id

    with bot.retrieve_data(user_id=user_id, chat_id=chat_id) as data:
        params = data["params"]

    if len(make_response(params=params)) == 1:

        with bot.retrieve_data(user_id=user_id, chat_id=chat_id) as data:
            data["id"] = make_response(params=params)[0]["id"]

        markup = types.InlineKeyboardMarkup(row_width=3)
        name = types.InlineKeyboardButton(text='Вывести названия', callback_data="list_name_product")
        description = types.InlineKeyboardButton(text='Вывести описание', callback_data="description")
        image = types.InlineKeyboardButton(text='Показать картинку', callback_data="image")
        product_link = types.InlineKeyboardButton(text='Ссылка на продукт ', callback_data="product_link")

        cancel = types.InlineKeyboardButton(text='Отмена', callback_data="cancel")

        markup.add(name, description, image, product_link, cancel)

        bot.send_message(chat_id=chat_id, text="Выберите, что хотите сделать", reply_markup=markup)

    elif 1 <= len(make_response(params=params)) <= 3:

        markup = types.InlineKeyboardMarkup(row_width=3)
        name = types.InlineKeyboardButton(text='Вывести названия', callback_data="list_name_product")
        cancel = types.InlineKeyboardButton(text='Отмена', callback_data="cancel")

        markup.add(name,  cancel)

        with bot.retrieve_data(user_id=user_id, chat_id=chat_id) as data:
            data["cond"] = "name_products"

        bot.send_message(chat_id=chat_id, text="Выберите, что хотите сделать", reply_markup=markup)

    else:
        bot.send_message(chat_id=call.message.chat.id, text=text.CONDITION)


@bot.callback_query_handler(func=lambda call: call.data in ["favorite"])
@exc_handler
def favorite_command_handler(call: types.CallbackQuery) -> None:
    """Обработчик, срабатываемый на нажитие клавиши favorite"""

    user_id = call.from_user.id
    chat_id = call.message.chat.id

    with bot.retrieve_data(user_id=user_id, chat_id=chat_id) as data:
        search_cond = data["search_cond"]
        user_choice = data["params"][search_cond]

        if search_cond == "brand":
            Favorite(user_id=user_id, brand=user_choice).save()
        elif search_cond == "product_tag":
            Favorite(user_id=user_id, product_tag=user_choice).save()
        elif search_cond == "product_type":
            Favorite(user_id=user_id, product_type=user_choice).save()

        logger.info(f"The user {user_id} added to favorites: {search_cond}: {user_choice}")

        bot.send_message(chat_id=chat_id, text=f"{search_cond}: {user_choice}")


@bot.callback_query_handler(func=lambda call: call.data in ["cancel_search_cond"])
@exc_handler
def call_btn_file(call: types.CallbackQuery) -> None:
    bot.set_state(user_id=call.from_user.id,
                  state=states.custom_states.UserState.condition_selection,
                  chat_id=call.message.chat.id)

    bot.delete_message(call.message.chat.id, call.message.id)


@bot.callback_query_handler(func=lambda call: call.data in ["website_link"])
def callback_web(call: types.CallbackQuery) -> None:
    """Обработка нажатия кнопки, перехода на сайт"""

    user_id = call.from_user.id
    chat_id = call.message.chat.id

    with bot.retrieve_data(user_id=user_id, chat_id=chat_id) as data:
        params = data["params"]

        urlkb = types.InlineKeyboardMarkup()
        urlButton = types.InlineKeyboardButton(text='Перейти на сайт', url=make_response(params=params)[0][call.data])
        cancel = types.InlineKeyboardButton(text='Отмена', callback_data='cancel')
        urlkb.add(urlButton, cancel)

        bot.send_message(chat_id=chat_id, text="Для перехода на сайт нажмите на кнопку", reply_markup=urlkb)
