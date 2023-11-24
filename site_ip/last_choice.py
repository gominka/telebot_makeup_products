from telebot import types

from database.models import History
from loader import bot
from site_ip.main_handler import make_response


@bot.callback_query_handler(func=lambda call: call.data in ["web_brand"])
def callback_web(call: types.CallbackQuery) -> None:
    """Обработка нажатия кнопки, перехода на сайт"""

    user_id = call.from_user.id
    chat_id = call.message.chat.id

    sql_select = History.select().order_by(History.id.desc()).where(History.user_id == user_id).get().brand
    fl = list(filter(lambda x: x['brand'] == sql_select, make_response(params={"brand": sql_select})))

    web_markup = types.InlineKeyboardMarkup()
    web_btn = types.InlineKeyboardButton("Перейти на сайт", url=fl[0]['website_link'])
    web_markup.add(web_btn)

    bot.send_message(chat_id=chat_id, text="Для перехода на сайт нажмите на кнопку", reply_markup=web_markup)

