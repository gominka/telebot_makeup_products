from telebot import types

from handlers.default_handlers.exception_handler import exc_handler
from loader import bot


@bot.callback_query_handler(func=lambda call: call.data in ["cancel"])
@exc_handler
def call_btn_file(call: types.CallbackQuery) -> None:
    bot.delete_message(call.message.chat.id, call.message.id)



