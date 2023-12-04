from keyboa.keyboards import keyboa_maker
from telebot import types
from telebot.types import ReplyKeyboardRemove

from handlers.default_handlers.exception_handler import exc_handler
from loader import bot
from site_ip.main_handler import BASE_PARAMS, conditions_list


@bot.message_handler(commands=['brand', 'product_tag', 'product_type'], state="*")
@exc_handler
def main_search_command(message: types.Message) -> None:
    """Обработчик, срабатываемый на команды /brand, /product_tag, /product_type, name"""
    msg_user = message.text[1:]
    user_id = message.from_user.id
    chat_id = message.chat.id
    ReplyKeyboardRemove()

    with bot.retrieve_data(user_id=user_id, chat_id=chat_id) as data:
        data["cond"] = msg_user
        try:
            data["params"]
        except KeyError:
            data["params"] = BASE_PARAMS

        finally:
            params = data["params"]
            cond = data["cond"]

    kb_cond = keyboa_maker(items=conditions_list(params=params, selected_condition=cond),
                           copy_text_to_callback=True, items_in_row=5)
    bot.send_message(chat_id=chat_id, reply_markup=kb_cond, text="Выберите условие")
