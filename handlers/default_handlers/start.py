from loader import bot

from telebot import types


@bot.message_handler(commands=['start'])
def bots_start(message: types.Message):
    print("1")
    markup = types.ReplyKeyboardMarkup(row_width=1)
    btn_1 = types.KeyboardButton(text='Бренд')
    btn_2 = types.KeyboardButton(text='Тэг')
    btn_th = types.KeyboardButton(text='Категория продукта')
    markup.add(btn_1, btn_2, btn_th)
    bot.send_message(message.chat.id, f'Приветствуем Вас, '
                                      f'{message.from_user.first_name}, '
                                      f'в нашем телеграм боте \n\n'
                                      f'Выберите условие для поиска', reply_markup=markup)




