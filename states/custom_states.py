from telebot.handler_backends import State, StatesGroup
from telebot import types

from handlers.default_handlers.exception_handler import exc_handler
from loader import bot
from site_ip.main_handler import make_response


class UserState(StatesGroup):
    search_state = State()
    custom_state = State()
    condition_selection = State()


@bot.message_handler(state=UserState.custom_state)
@exc_handler
def search_in_file(message: types.Message) -> None:
    with bot.retrieve_data(user_id=message.from_user.id, chat_id=message.chat.id) as data:
        params = data["params"]
        data = make_response(params)
        print(data)
