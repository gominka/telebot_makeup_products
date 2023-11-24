from telebot.types import CallbackQuery

from keyboards.inline.sec import odin
from loader import bot

from site_ip.main_handler import make_response
from user_interface import text


@bot.callback_query_handler(func=lambda call: call.data in ["branding", "tagging", "typing"])
def check_in_site_call(call: CallbackQuery) -> None:
    """

    :param
        call: CallbackQuery
    :return: None
    """

    user_id = call.from_user.id
    chat_id = call.message.chat.id

    with bot.retrieve_data(user_id=user_id, chat_id=chat_id) as data:
        params = data["params"]
        print(params)

    if len(make_response(params=params)) == 1:
        bot.send_message(
            chat_id=chat_id,
            text="Выберите, что хотите сделать",
            reply_markup=odin()
        )
    else:
        bot.send_message(
            chat_id=call.message.chat.id,
            text=text.COND
        )



@bot.callback_query_handler(func=lambda call: call.data in ["price", "rating", "api_featured_image", "product_link", "description"])
def call_btn_file(call: CallbackQuery) -> None:
    """
      :param call:
      :return: None
    """

    user_id = call.from_user.id
    chat_id = call.message.chat.id

    with bot.retrieve_data(user_id=user_id, chat_id=chat_id) as data:
        params = data["params"]
        print(params)

    bot.send_message(chat_id=chat_id, text=name_handler(params=params, cond=call.data))
