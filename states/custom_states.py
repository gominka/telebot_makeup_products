from telebot.handler_backends import State, StatesGroup


class UserState(StatesGroup):
    search_state = State()
    custom_state = State()
    condition_selection = State()


