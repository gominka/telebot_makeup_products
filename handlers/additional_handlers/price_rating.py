from telebot import types

from handlers.default_handlers.exception_handler import exc_handler
from keyboards.reply import reply_keyboards
from loader import bot
from states.custom_states import UserState


@bot.message_handler(commands=['high', 'low'])
@exc_handler
def main_search_command(message: types.Message) -> None:
    """Обработчик, срабатываемый на команды /high, /low"""

    msg_user = message.text[1:]
    user_id = message.from_user.id
    chat_id = message.chat.id

    with bot.retrieve_data(user_id=user_id, chat_id=chat_id) as data:
        if msg_user == "high":
            data["cond"] = "_less_than"

        else:
            data["cond"] = "_greater_than"

        msg = bot.send_message(chat_id=chat_id, text="Выберете условие: ",
                               reply_markup=reply_keyboards.get_reply_keyboard(["rating", "price"]))
        bot.register_next_step_handler(msg, select_condition)


def select_condition(message: types.Message) -> None:
    msg_user = message.text
    user_id = message.from_user.id
    chat_id = message.chat.id

    with bot.retrieve_data(user_id=user_id, chat_id=chat_id) as data:
            data["cond"] = f"{msg_user}_less_than"
            print(data["cond"])


    bot.send_message(chat_id=message.chat.id, text="Введите значение: ", reply_markup=reply_keyboards.EMPTY)

    msg_user = message.text
    user_id = message.from_user.id
    chat_id = message.chat.id

    with bot.retrieve_data(user_id=user_id, chat_id=chat_id) as data:
        data["cond"] = msg_user

    bot.set_state(user_id=message.from_user.id, state=UserState.condition_selection, chat_id=message.chat.id)


@bot.message_handler(state=UserState.condition_selection, is_digit=True)
@exc_handler
def search_in_file(message: types.Message) -> None:
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        msg = ("Ready, take a look:\n<b>"
               f"Name: {data['name']}\n"
               f"Surname: {data['surname']}\n"
               f"Age: {message.text}</b>")
        bot.send_message(message.chat.id, msg, parse_mode="html")
    bot.delete_state(message.from_user.id, message.chat.id)

