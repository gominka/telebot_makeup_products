from telebot.handler_backends import State, StatesGroup
from telebot import types

from handlers.default_handlers.exception_handler import exc_handler
from loader import bot
from site_ip.main_handler import make_response


class UserState(StatesGroup):
    search_state = State()
    custom_state = State()
    condition_selection = State()


