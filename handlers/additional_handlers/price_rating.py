from telebot import types

from handlers.default_handlers.exception_handler import exc_handler
from keyboards.reply import reply_keyboards
from loader import bot
from states.custom_states import UserState


@bot.message_handler(commands=['high', 'low'], state="*")
@exc_handler
def main_search_command(message: types.Message) -> None:
    """Обработчик, срабатываемый на команды /high, /low"""

    msg_user = message.text[1:]
    user_id = message.from_user.id
    chat_id = message.chat.id

    with bot.retrieve_data(user_id=user_id, chat_id=chat_id) as data:
        data["cond"] = msg_user

        msg = bot.send_message(chat_id=chat_id, text="Выберете условие: ",
                               reply_markup=reply_keyboards.get_reply_keyboard(["Rating", "Price"]))
        bot.register_next_step_handler(msg, select_condition)


def select_condition(message: types.Message) -> None:
    bot.send_message(chat_id=message.chat.id, text="Введите значение: ", reply_markup=reply_keyboards.EMPTY)
    bot.set_state(user_id=message.from_user.id, state=UserState.condition_selection, chat_id=message.chat.id)
