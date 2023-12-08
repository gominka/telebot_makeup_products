from telebot import types

from handlers.default_handlers.exception_handler import exc_handler
from keyboards.reply import reply_keyboards
from loader import bot


@bot.message_handler(commands=['high', 'low'])
@exc_handler
def main_search_command(message: types.Message) -> None:
    """The handler triggered by the command /high, /low"""

    msg_user = message.text[1:]
    user_id = message.from_user.id
    chat_id = message.chat.id

    with bot.retrieve_data(user_id=user_id, chat_id=chat_id) as data:
        if msg_user == "high":
            data["cond2"] = "_less_than"

        else:
            data["cond2"] = "_greater_than"

        msg = bot.send_message(chat_id=chat_id, text="Choose a condition: ",
                               reply_markup=reply_keyboards.get_reply_keyboard(["rating", "price"]))
        bot.register_next_step_handler(msg, select_condition)


def select_condition(message: types.Message) -> None:
    msg_user = message.text
    user_id = message.from_user.id
    chat_id = message.chat.id

    with bot.retrieve_data(user_id=user_id, chat_id=chat_id) as data:
        data["cond1"] = msg_user

    msg = bot.send_message(chat_id=message.chat.id, text="Enter a value: ", reply_markup=reply_keyboards.EMPTY)

    bot.register_next_step_handler(msg, select_cond)


def select_cond(message: types.Message) -> None:
    msg_user = int(message.text)
    user_id = message.from_user.id
    chat_id = message.chat.id

    with bot.retrieve_data(user_id=user_id, chat_id=chat_id) as data:
        if data["cond1"] == "rating" and 1 <= msg_user <= 10:
            cond = data["cond1"]+data["cond2"]
            print(cond)
            data["params"][cond] == msg_user



