import requests
from telebot.types import CallbackQuery

from database.models import History
from keyboards.inline.sec import odin
from loader import bot
from site_ip.response_main import name_handler


@bot.callback_query_handler(func=lambda call: call.data in ["branding"])
def history_command_callback(call: CallbackQuery) -> None:
    """

    :param call: CallbackQuery
    :return: None
    """

    user_id = call.from_user.id
    chat_id = call.message.chat.id

    with bot.retrieve_data(user_id=user_id, chat_id=chat_id) as data:
        msg_user = data["brand"]

    # TODO: сформировать ссылку
    url = "http://makeup-api.herokuapp.com/api/v1/products.json?brand={}".format(msg_user)
    response = requests.get(url)
    url_data = response.json()

    with bot.retrieve_data(user_id=user_id, chat_id=chat_id) as data:
        data["url_data"] = url_data

    if len(url_data) == 1:
        bot.send_message(
            chat_id=call.message.chat.id,
            text="Выберите, что хотите сделать",
            reply_markup=odin()
        )
    else:
        # TODO: сортировать по рейтингу, цене ...
        print("Несколько вариантов")


@bot.callback_query_handler(
    func=lambda call: call.data in ["price", "rating", "api_featured_image", "product_link", "description"])
def call_btn_file(call: CallbackQuery) -> None:
    """

      :param call:
      :return: None
    """
    user_id = call.from_user.id
    chat_id = call.message.chat.id

    with bot.retrieve_data(user_id=user_id, chat_id=chat_id) as data:
        url_data = data["url_data"]

    bot.send_message(chat_id=call.message.chat.id, text=name_handler(url_data, call.data))
