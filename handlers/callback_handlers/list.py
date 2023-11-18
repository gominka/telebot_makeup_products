from keyboa.keyboards import keyboa_maker
from loguru import logger
from peewee import IntegrityError
from telebot.types import CallbackQuery

from database.models import History
from keyboards.inline.main_comm_inline_markup import search_inline_markup, web_inline_btn
from loader import bot
from site_ip.testt import cond_handler


@bot.callback_query_handler(func=lambda call: call.data in [
    "list_brand",
    "list_tag",
    "list_product_type"])
def btn_list_condition(call: CallbackQuery) -> None:
    """

    :param call:
    :return:
    """

    user_id = call.from_user.id
    chat_id = call.message.chat.id

    with bot.retrieve_data(user_id=user_id, chat_id=chat_id) as data:
        msg_user = data["first_cond"]

    kb_cond = keyboa_maker(
            items=cond_handler(msg_user),
            copy_text_to_callback=True,
            items_in_row=4
        )

    bot.send_message(
        chat_id=call.message.chat.id,
        reply_markup=kb_cond,
        text="Выберите условие"
    )

