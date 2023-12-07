from telebot import types

from loader import bot
from site_ip.main_handler import make_response
from user_interface.text import DESCRIPTION



@bot.callback_query_handler(func=lambda call: call.data in ["description"])
def call_btn_file(call: types.CallbackQuery) -> None:
    user_id = call.from_user.id
    chat_id = call.message.chat.id

    with bot.retrieve_data(user_id=user_id, chat_id=chat_id) as data:
        params = data["params"]

    bot.send_photo(chat_id, make_response(params=params)[0]["api_featured_image"])
    bot.send_message(chat_id=chat_id, text=DESCRIPTION.format(
        make_response(params=params)[0]["description"],
        make_response(params=params)[0]["api_featured_image"]))
