from keyboa.keyboards import keyboa_maker
from loguru import logger
from peewee import IntegrityError
from telebot.types import CallbackQuery

from database.models import History
from keyboards.inline.main_comm_inline_markup import search_inline_markup, web_inline_btn
from loader import bot
from site_ip.response_main import main_handler, brand_handler


@bot.callback_query_handler(func=lambda call: call.data in ["list_brand"])
def user_select_brand(call) -> None:
    kb_brands = keyboa_maker(
        items=brand_handler(),
        copy_text_to_callback=True,
        items_in_row=4
    )
    bot.send_message(
        chat_id=call.message.chat.id,
        reply_markup=kb_brands,
        text="Выберете бренд"
    )


@bot.callback_query_handler(func=lambda call: call.data in brand_handler())
def brand_condition_search(call: CallbackQuery) -> None:
    """

      :param call:
      :return: None
    """

    try:
        user_id = call.from_user.id
        History(brand=call.data, user_id=user_id).save()

        bot.send_message(call.message.chat.id,
                         "Выберете опцию: ",
                         reply_markup=search_inline_markup(call.message))

        logger.info(f'Выбран бренд. User_id: {user_id}, Brand: {call.data}')

    except IntegrityError:
        # user_id = call.from_user.id
        # Conditions(brand_cond=None, user_id=user_id)
        # cond.save()
        bot.reply_to(message=call.message,
                     text="dddd")


@bot.callback_query_handler(func=lambda call: call.data in ["web"])
def callback_web(call: CallbackQuery) -> None:
    user_id = call.from_user.id
    chat_id = call.message.chat.id

    try:
        sql_select = History.select().where(History.user_id == user_id).get()
        print(History.select(History.brand).where(History.id == "1").get())
        fl = list(filter(lambda x: x['brand'] == sql_select, main_handler()))
        bot.send_message(
            chat_id=chat_id,
            text="Для перехода на сайт нажмите на кнопку",
            reply_markup=web_inline_btn(fl)
        )

    except TypeError:
        bot.send_message(call.message.chat.id, "Ошибка")

