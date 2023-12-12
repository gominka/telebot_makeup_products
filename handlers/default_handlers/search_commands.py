from keyboa.keyboards import keyboa_maker

from telebot import types

import states
from handlers.default_handlers.exception_handler import exc_handler
from loader import bot
from site_ip.main_request import BASE_PARAMS, conditions_list


@bot.message_handler(commands=['brand', 'product_tag', 'product_type'], state="*")
@exc_handler
def search_command_handler(message: types.Message) -> None:
    """The handler triggered by the commands /brand, /product_tag, /product_type"""

    msg_user = message.text[1:]
    user_id = message.from_user.id
    chat_id = message.chat.id

    with bot.retrieve_data(user_id=user_id, chat_id=chat_id) as data:
        data["search_cond"] = msg_user
        try:
            data["params"]
        except KeyError:
            data["params"] = BASE_PARAMS

        finally:
            params = data["params"]
            search_cond = data["search_cond"]

    kb_cond = keyboa_maker(items=conditions_list(params=params, selected_condition=search_cond),
                           copy_text_to_callback=True, items_in_row=5)

    bot.set_state(user_id=user_id, state=states.custom_states.UserState.condition_selection, chat_id=chat_id)

    bot.send_message(chat_id=chat_id, reply_markup=kb_cond, text="Select a condition:  ")


@bot.callback_query_handler(func=lambda call: True, state=states.custom_states.UserState.condition_selection)
@exc_handler
def callback_search_command(call: types.CallbackQuery) -> None:
    """Processing button clicks, condition selection"""

    user_id = call.from_user.id
    chat_id = call.message.chat.id

    with bot.retrieve_data(user_id=user_id, chat_id=chat_id) as data:
        search_cond = data["search_cond"]
        data["params"][search_cond] = call.data

        search_command_markup = types.InlineKeyboardMarkup(row_width=2)
        custom_search = types.InlineKeyboardButton(text='Continue the search', callback_data="check_amount_products")
        cancel = types.InlineKeyboardButton(text='Cancel', callback_data='cancel_search_cond')

        if search_cond == "brand":
            website = types.InlineKeyboardButton(text='Website brand', callback_data="website_link")
            search_command_markup.add(custom_search, website)

        else:
            search_command_markup.add(custom_search)

        search_command_markup.add(cancel)
        bot.send_message(chat_id=chat_id, text="Select a condition ", reply_markup=search_command_markup)

        bot.set_state(user_id=user_id, state=states.custom_states.UserState.custom_state, chat_id=chat_id)