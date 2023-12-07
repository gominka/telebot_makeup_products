from telebot import types

from loader import bot
from site_ip.main_handler import make_response


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
        cancel = types.InlineKeyboardButton(text='Отмена', callback_data='cancel')
        urlkb.add(urlButton, cancel)

        bot.send_message(chat_id=chat_id, text="Для перехода на сайт нажмите на кнопку", reply_markup=urlkb)

