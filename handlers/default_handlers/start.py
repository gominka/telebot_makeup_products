from telebot import types

from loader import bot
from handlers.additional_handlers import brand, tag

text_messages = {
    'start':
        u'Добро пожаловать {name}!\n\n'
        u'Для продолжения нажмите на кнопку\n\n',
}


@bot.message_handler(commands=['start'])
def bot_start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    btn_1 = types.KeyboardButton(text='Поиск товара по бренду')
    btn_2 = types.KeyboardButton(text='Поиск товара по тэгу')
    markup.add(btn_1, btn_2)
    bot.send_message(message.chat.id, f'<i> Приветствуем Вас, '
                                      f'<b> {message.from_user.first_name}</b>, '
                                      f'в нашем телеграм боте </i>', parse_mode='html', reply_markup=markup)

    bot.register_next_step_handler(message, txt)


def txt(message: types.Message):
    if message.text == "Поиск товара по бренду":
        brand.brand(message)
    elif message.text == "Поиск товара по тэгу":
        tag.tag(message)
