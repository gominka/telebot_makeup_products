from telebot import types

from loader import bot


@bot.message_handler(commands=['low'])
def low(message: types.Message):
    """
        Команда, выводящая значения по заданному минимальному условтию, стоимости или рейтингу
        :param message:
        :return:
        """
    markup = types.InlineKeyboardMarkup(row_width=1)
    btnPrice = types.InlineKeyboardButton(text='Фильтр по цене',
                                          callback_data="price")
    btnRat = types.InlineKeyboardButton(text='Фильтр по рейтингу',
                                        callback_data='rating')
    markup.add(btnPrice, btnRat)
    bot.send_message(message.chat.id, 'Выберите опцию:', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == ['price', 'rating'])
def callback_min(call: types.CallbackQuery):
    maxMean = bot.send_message(call.message.chat.id, "Выберите минимальное значение: ")  # 1-10
    cid = call.message.chat.id
    if call.data == "price":
        bot.register_next_step_handler(maxMean, find_price)
    elif call.data == "rating":
        bot.register_next_step_handler(maxMean, find_rat)


def find_price(message: types.Message):
    bot.send_message(message.chat.id, "Идёт поиск: ")


def find_rat(message: types.Message):
    bot.send_message(message.chat.id, "Идёт поиск: ")
