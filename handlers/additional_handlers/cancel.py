from telebot.types import Message

from loader import bot


CANCEL_CHANGE = "Cancelled! Your data is not changed."


@bot.message_handler(commands=['cancel'], states="*")
def handle_cancel_comm_data(message: Message) -> None:
    bot.delete_state(message.from_user.id, message.chat.id)
    bot.send_message(
        message.chat.id,
        CANCEL_CHANGE)