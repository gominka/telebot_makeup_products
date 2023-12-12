from keyboa.keyboards import keyboa_maker
from telebot import types

import states
from handlers.default_handlers.exception_handler import exc_handler
from loader import bot
from site_ip.main_request import make_response, conditions_list
from user_interface import text
from user_interface.text import DESCRIPTION


@bot.callback_query_handler(func=lambda call: call.data in ["check_amount_products"])
def check_amount_products(call: types.CallbackQuery) -> None:
    """Processing of the output button with a callback check_amount_products"""

    user_id = call.from_user.id
    chat_id = call.message.chat.id

    with bot.retrieve_data(user_id=user_id, chat_id=chat_id) as data:
        params = data["params"]

    if len(make_response(params=params)) == 1:

        bot.send_message(chat_id=chat_id, text=DESCRIPTION.format(
            make_response(params=params)[0]["name"],
            make_response(params=params)[0]["price"],
            make_response(params=params)[0]["description"],
            make_response(params=params)[0]["product_link"]))

    elif 1 <= len(make_response(params=params)) <= 3:
        kb_cond = keyboa_maker(items=conditions_list(params=params, selected_condition="list_name_product"),
                               copy_text_to_callback=True, items_in_row=5)

        bot.set_state(user_id=user_id, state=states.custom_states.UserState.final_selection, chat_id=chat_id)

        bot.send_message(chat_id=chat_id, reply_markup=kb_cond, text="Select a name:  ")

    else:
        bot.send_message(chat_id=call.message.chat.id, text=text.CONDITION)


@bot.callback_query_handler(func=lambda call: True, state=states.custom_states.UserState.final_selection)
@exc_handler
def callback_search_command(call: types.CallbackQuery) -> None:
    """Processing button clicks, condition selection"""

    user_id = call.from_user.id
    chat_id = call.message.chat.id

    with bot.retrieve_data(user_id=user_id, chat_id=chat_id) as data:
        data["params"]["name"] = call.data
        params = data["params"]

        bot.send_message(chat_id=chat_id, text=DESCRIPTION.format(
            make_response(params=params)[0]["name"],
            make_response(params=params)[0]["price"],
            make_response(params=params)[0]["description"],
            make_response(params=params)[0]["product_link"]))

    bot.set_state(user_id=user_id, state=states.custom_states.UserState.custom_state, chat_id=chat_id)


@bot.callback_query_handler(func=lambda call: call.data in ["cancel_search_cond"])
@exc_handler
def call_btn_file(call: types.CallbackQuery) -> None:
    bot.set_state(user_id=call.from_user.id,
                  state=states.custom_states.UserState.condition_selection,
                  chat_id=call.message.chat.id)

    bot.delete_message(call.message.chat.id, call.message.id)


@bot.callback_query_handler(func=lambda call: call.data in ["website_link"])
def callback_web(call: types.CallbackQuery) -> None:
    """Processing of a button click, a link to the site"""

    user_id = call.from_user.id
    chat_id = call.message.chat.id

    with bot.retrieve_data(user_id=user_id, chat_id=chat_id) as data:
        params = data["params"]

        urlkb = types.InlineKeyboardMarkup()
        urlButton = types.InlineKeyboardButton(text='Перейти на сайт', url=make_response(params=params)[0][call.data])
        cancel = types.InlineKeyboardButton(text='Отмена', callback_data='cancel')
        urlkb.add(urlButton, cancel)

        bot.send_message(chat_id=chat_id, text="Для перехода на сайт нажмите на кнопку", reply_markup=urlkb)
