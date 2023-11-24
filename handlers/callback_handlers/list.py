from keyboa.keyboards import keyboa_maker
from loguru import logger
from telebot import types

from database.models import History
from handlers.default_handlers.exception_handler import exc_handler
from loader import bot
from site_ip.main_handler import BASE_PARAMS, conditions_list


@bot.callback_query_handler(func=lambda call: call.data in ["list_brand", "list_product_tag", "list_product_type"])
def callback_handler_condition(call: types.CallbackQuery) -> None:
    """Обработка нажатия кнопок, выводящая Inline клавиатуру с выбранным условием"""

    user_id = call.from_user.id
    chat_id = call.message.chat.id

    with bot.retrieve_data(user_id=user_id, chat_id=chat_id) as data:
        cond = data["cond"]
        params = data["params"]

    kb_cond = keyboa_maker(items=conditions_list(params=params, selected_condition=cond),
                           copy_text_to_callback=True, items_in_row=5)
    bot.send_message(chat_id=chat_id, reply_markup=kb_cond, text="Выберите условие")


@bot.callback_query_handler(func=lambda call: call.data in conditions_list(params=BASE_PARAMS,
                                                                           selected_condition="all_condition"))
@exc_handler
def call_btn_file(call: types.CallbackQuery) -> None:
    """Обработка нажатия кнопок, выбора условия"""

    user_id = call.from_user.id
    chat_id = call.message.chat.id
    msg_user = call.data

    with bot.retrieve_data(user_id=user_id, chat_id=chat_id) as data:
        cond = data["cond"]

        markup = types.InlineKeyboardMarkup(row_width=1)
        custom_search = types.InlineKeyboardButton(text='Поиск товаров', callback_data="branding")
        website_brand = types.InlineKeyboardButton(text='Переход на сайт бренда', callback_data="web_brand")
        cancel = types.InlineKeyboardButton(text='Отмена', callback_data='cancel_request')

        if cond == "brand":
            markup.add(custom_search, website_brand, cancel)
            if History.get_or_none(History.user_id == user_id) is None:
                History(brand=call.data, user_id=user_id).save()
            elif History.select().order_by(History.id.desc()).where(History.user_id == user_id).get().brand == "null":
                History.update(brand=call.data).where(History.user_id == user_id).execute()
            else:
                History(brand=call.data, user_id=user_id).save()
            data["params"]["brand"] = call.data.replace(' ', '%20')
            logger.info(f'Выбран бренд. User_id: {user_id}, Brand: {msg_user}')

        elif cond == "product_tag":
            markup.add(custom_search, cancel)

            History(produst_tag=call.data, user_id=user_id).save()
            data["params"]["product_tag"] = call.data.replace(' ', '%20')
            logger.info(f'Выбран тэг. User_id: {user_id}, Product_tag: {msg_user}')

        elif cond == "product_type":
            markup.add(custom_search, cancel)

            History(product_type=call.data, user_id=user_id).save()
            data["params"]["product_type"] = call.data.replace(' ', '%20')
            logger.info(f'Выбран тип продукта. User_id: {user_id}, Product_type: {msg_user}')

        bot.send_message(chat_id=chat_id, text="Выберете опцию: ", reply_markup=markup)

        # if History.get_or_none(History.user_id == user_id) is None:
        #     History(brand=call.data.replace(' ', '%20'), user_id=user_id).save()
        #
        # else:
        #     History.update(brand=call.data.replace(' ', '%20')).where(History.user_id == user_id).execute()
