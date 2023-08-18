from telebot.types import Message

from loader import bot

@bot.message_handler(commands=["hello-world"])
def hello_world_message(message: Message) -> None:
    text = f'Добро пожаловать, {message.from_user.first_name})'
    bot.send_message(message.chat.id, text)

