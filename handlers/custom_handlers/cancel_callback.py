from telebot import types

import states
from handlers.default_handlers.exception_handler import exc_handler
from loader import bot


@bot.callback_query_handler(func=lambda call: call.data in ["cancel"])
@exc_handler
def call_btn_file(call: types.CallbackQuery) -> None:
    bot.delete_message(call.message.chat.id, call.message.id)


@bot.callback_query_handler(func=lambda call: call.data in ["cancel_search_cond"])
@exc_handler
def call_btn_file(call: types.CallbackQuery) -> None:
    bot.set_state(user_id=call.from_user.id,
                  state=states.custom_states.UserState.condition_selection,
                  chat_id=call.message.chat.id)

    bot.delete_message(call.message.chat.id, call.message.id)
