from telebot.types import CallbackQuery

from database.models import History
from keyboards.inline.main_comm_inline_markup import web_inline_btn
from loader import bot
from site_ip.response_main import main_handler


@bot.callback_query_handler(func=lambda call: call.data in ["web"])
def callback_web(call: CallbackQuery) -> None:

    user_id = call.from_user.id
    chat_id = call.message.chat.id

    try:
        sql_select = History.select().order_by(History.id.desc()).where(History.user_id == user_id).get().brand
        fl = list(filter(lambda x: x['brand'] == sql_select, main_handler()))
        bot.send_message(
            chat_id=chat_id,
            text="Для перехода на сайт нажмите на кнопку",
            reply_markup=web_inline_btn(fl)
        )

    except Exception:
        # TODO: уже есть в базе
        bot.send_message(call.message.chat.id, Exception)
