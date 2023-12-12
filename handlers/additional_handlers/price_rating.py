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

    msg = bot.send_message(chat_id=message.chat.id, text="Enter a number: ", reply_markup=reply_keyboards.EMPTY)

    bot.register_next_step_handler(msg, select_cond)


@exc_handler
def select_cond(message: types.Message) -> None:

    msg_user = int(message.text)
    user_id = message.from_user.id
    chat_id = message.chat.id

    with bot.retrieve_data(user_id=user_id, chat_id=chat_id) as data:
        if (data["cond1"] == "rating" and 1 <= msg_user <= 10) or data["cond1"] == "price":
            cond = data["cond1"]+data["cond2"]
            data["params"][cond] = msg_user

        elif data["cond1"] == "rating":
            bot.send_message(chat_id=message.chat.id, text="Enter a number from 1 to 10: ", reply_markup=reply_keyboards.EMPTY)
            select_condition(message)

    search_command_markup = types.InlineKeyboardMarkup(row_width=3)
    custom_search = types.InlineKeyboardButton(text='Continue the search', callback_data="check_amount_products")
    cancel = types.InlineKeyboardButton(text='Cancel', callback_data='cancel_search_cond')
    search_command_markup.add(custom_search, cancel)

    bot.send_message(chat_id=chat_id, text="Select a condition ", reply_markup=search_command_markup)


