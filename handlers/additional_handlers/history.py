from telebot.types import Message


from database.models import User, Conditions
from handlers.callback_handlers import history
from keyboards.inline.history import inline_btn_history
from loader import bot


@bot.message_handler(state="*", commands=['history'])
def brand(message: Message) -> None:
    """
    Обработчик команды, срабатываемый на /history

    :param message:
    :return: None
    """

    if User.get_or_none(User.user_id == message.from_user.id) is None:
        bot.reply_to(message, "Вы не зарегистрированы. Напишите /start")
        return

    bot.send_message(message.chat.id, "Выберите условие: ", reply_markup=inline_btn_history())




