from keyboa.keyboards import keyboa_maker
from loguru import logger

from telebot import types

import states
from handlers.default_handlers.exception_handler import exc_handler
from loader import bot
from site_ip.main_handler import BASE_PARAMS, conditions_list


@bot.message_handler(commands=['brand', 'product_tag', 'product_type'], state="*")
@exc_handler
def search_command_handler(message: types.Message) -> None:
    """Обработчик, срабатываемый на команды /brand, /product_tag, /product_type"""

    msg_user = message.text[1:]
    user_id = message.from_user.id
    chat_id = message.chat.id

    with bot.retrieve_data(user_id=user_id, chat_id=chat_id) as data:
        data["search_cond"] = msg_user
        try:
            data["params"]
        except KeyError:
            data["params"] = BASE_PARAMS

        finally:
            params = data["params"]
            search_cond = data["search_cond"]

    kb_cond = keyboa_maker(items=conditions_list(params=params, selected_condition=search_cond),
                           copy_text_to_callback=True, items_in_row=5)

    bot.set_state(user_id=user_id, state=states.custom_states.UserState.condition_selection, chat_id=chat_id)

    bot.send_message(chat_id=chat_id, reply_markup=kb_cond, text="Выберите условие:  ")


@bot.callback_query_handler(func=lambda call: True, state=states.custom_states.UserState.condition_selection)
@exc_handler
def callback_search_command(call: types.CallbackQuery) -> None:
    """Обработка нажатия кнопок, выбора условия"""
    user_id = call.from_user.id
    chat_id = call.message.chat.id
    msg_user = call.data

    with bot.retrieve_data(user_id=user_id, chat_id=chat_id) as data:
        search_cond = data["search_cond"]

        markup = types.InlineKeyboardMarkup(row_width=1)
        custom_search = types.InlineKeyboardButton(text='Продолжить поиск', callback_data="check_amount_products")
        favourite = types.InlineKeyboardButton(text='Добавить в избранное', callback_data="favorite")
        cancel = types.InlineKeyboardButton(text='Отмена', callback_data='cancel_search_cond')
        markup.add(custom_search, favourite)

        if search_cond == "brand":
            website = types.InlineKeyboardButton(text='Переход на сайт бренда', callback_data="website_link")
            markup.add(website)

        markup.add(cancel)
        bot.send_message(chat_id=chat_id, text="Что хотите сделать? ", reply_markup=markup)

        data["params"][search_cond] = call.data
        bot.set_state(user_id=user_id, state=states.custom_states.UserState.custom_state, chat_id=chat_id)
