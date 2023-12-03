from telebot import types

from loader import bot
from site_ip.main_handler import make_response
from user_interface.text import DESCRIPTION


@bot.callback_query_handler(func=lambda call: call.data in ["website_link", "product_link"])
def callback_web(call: types.CallbackQuery) -> None:
    """Обработка нажатия кнопки, перехода на сайт"""

    user_id = call.from_user.id
    chat_id = call.message.chat.id


    with bot.retrieve_data(user_id=user_id, chat_id=chat_id) as data:
        params = data["params"]
        data["id"] = make_response(params=params)[0]["id"]
        print()

        urlkb = types.InlineKeyboardMarkup(row_width=1)
        urlButton = types.InlineKeyboardButton(text='Перейти на сайт',
                                               url=make_response(params=params)[0][call.data])
        urlkb.add(urlButton)

        bot.send_message(chat_id=chat_id, text="Для перехода на сайт нажмите на кнопку", reply_markup=urlkb)


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
