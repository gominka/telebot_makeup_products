from telebot import types

from handlers.default_handlers.exception_handler import exc_handler
from keyboards.reply import reply_keyboards
from loader import bot


@bot.message_handler(commands=['high', 'low'])
@exc_handler
def main_search_command(message: types.Message) -> None:
    """Обработчик, срабатываемый на команды /high, /low"""

    msg_user = message.text[1:]
    user_id = message.from_user.id
    chat_id = message.chat.id

    with bot.retrieve_data(user_id=user_id, chat_id=chat_id) as data:
        if msg_user == "high":
            data["cond2"] = "_less_than"

        else:
            data["cond2"] = "_greater_than"

        msg = bot.send_message(chat_id=chat_id, text="Выберете условие: ",
                               reply_markup=reply_keyboards.get_reply_keyboard(["rating", "price"]))
        bot.register_next_step_handler(msg, select_condition)


def select_condition(message: types.Message) -> None:
    msg_user = message.text
    user_id = message.from_user.id
    chat_id = message.chat.id

    with bot.retrieve_data(user_id=user_id, chat_id=chat_id) as data:
            data["cond1"] = msg_user
            print(data["cond1"])

    msg = bot.send_message(chat_id=message.chat.id, text="Введите значение: ", reply_markup=reply_keyboards.EMPTY)

    bot.register_next_step_handler(msg, select_cond)


def select_cond(message: types.Message) -> None:
    msg_user = message.text
    user_id = message.from_user.id
    chat_id = message.chat.id

    with bot.retrieve_data(user_id=user_id, chat_id=chat_id) as data:
            print(data["cond1"]+data["cond2"])



