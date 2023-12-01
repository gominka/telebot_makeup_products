from telebot import types
from telebot.types import ReplyKeyboardRemove

from handlers.default_handlers.exception_handler import exc_handler
from loader import bot
from site_ip.main_handler import BASE_PARAMS
from states.custom_states import UserState


@bot.message_handler(commands=['brand', 'product_tag', 'product_type', 'name'], state="*")
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

    if msg_user == "name":
        bot.send_message(chat_id=chat_id, text="Введите название: ")
        bot.set_state(user_id=user_id, state=UserState.custom_state, chat_id=chat_id)

    else:
        main_search_markup = types.InlineKeyboardMarkup(row_width=2)
        user_selection = types.InlineKeyboardButton(text='Ввести самостоятельно',
                                                    callback_data='user_search_{}'.format(msg_user))
        system_selection = types.InlineKeyboardButton(text='Выбрать из представленных',
                                                      callback_data='list_{}'.format(msg_user))
        cancel = types.InlineKeyboardButton(text='Отмена', callback_data="cancel")
        main_search_markup.add(user_selection, system_selection, cancel)

        bot.send_message(chat_id=chat_id, text="Выберете условие для продолжения поиска: ",
                         reply_markup=main_search_markup)
