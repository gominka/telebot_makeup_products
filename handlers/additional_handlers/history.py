from keyboa.keyboards import keyboa_maker
from telebot import types
from telebot.types import Message

import states
from database.models import History
from handlers.additional_handlers.search_callback import send_product_details
from handlers.default_handlers.exception_handler import exc_handler
from site_ip.main_request import make_response, BASE_PARAMS
from loader import bot


@bot.message_handler(commands=['history'], state="*")
@exc_handler
def start_command_handler(message: Message) -> None:
    """Handler for the /start command."""

    product_names = set([name for name in History.select().where(History.user_id == message.from_user.id)])

    bot.send_message(message.chat.id, text="You have previously selected the following products:\n\n",
                     reply_markup=keyboa_maker(items=list(product_names),
                                               copy_text_to_callback=True, items_in_row=5))

    bot.set_state(user_id=message.from_user.id,
                  state=states.custom_states.UserState.product_details,
                  chat_id=message.chat.id)


@bot.callback_query_handler(func=None, state=states.custom_states.UserState.product_details)
def callback_search_command(call: types.CallbackQuery) -> None:
    """Processing button clicks, name product selection"""
    user_id = call.from_user.id
    chat_id = call.message.chat.id

    params = BASE_PARAMS
    params["name"] = call.data
    response = make_response(params=params)
    send_product_details(chat_id, response[0])

    bot.set_state(user_id=user_id, state=states.custom_states.UserState.custom_state, chat_id=chat_id)
