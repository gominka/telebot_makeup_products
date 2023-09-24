from telebot import types

from handlers.additional_handlers.high import callback_max
from handlers.additional_handlers.low import callback_min
from loader import bot


@bot.message_handler(commands=['custom'])
def custom(message: types.Message) -> None:
    markup = types.InlineKeyboardMarkup(row_width=1)
    btnPrice = types.InlineKeyboardButton(text='Фильтр по цене',
                                          callback_data="custom_price")
    btnRat = types.InlineKeyboardButton(text='Фильтр по рейтингу',
                                        callback_data='custom_rating')
    markup.add(btnPrice, btnRat)
    bot.send_message(message.chat.id, 'Выберите опцию:', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def answer(call: types.CallbackQuery):
    cid = call.message.chat.id
    if call.data == "custom_price":
        f = callback_min(call)

        # markup = types.InlineKeyboardMarkup(row_width=1)
        # custBtn = types.InlineKeyboardButton(text='Ввести диапазон цен',
        #                                      callback_data="cust")
        # minBtn = types.InlineKeyboardButton(text='Ввести только максимальное значение',
        #                                     callback_data='min')
        # maxBtn = types.InlineKeyboardButton(text='Ввести только максимальное значение',
        #                                     callback_data="max")
        # markup.add(custBtn, minBtn, maxBtn)
        # bot.send_message(call.message.chat.id, 'Выберите опцию:', reply_markup=markup)
    elif call.data == "custom_rating":
        f = callback_min(call)
#     elif call.data == "cust":
#         msglow = bot.send_message(call.message.chat.id, 'Введите минимальную стоимость:')
#         bot.register_next_step_handler(msglow)
#         msghigh = bot.send_message(call.message.chat.id, 'Введите максимальную стоимость:')
#         url = "http://makeup-api.herokuapp.com/api/v1/products.json?price_greater_than={}&price_less_than={}".format(
#             msglow,
#             msghigh)
#         response = requests.get(url)
#         data = response.json()
#         listPrice = [item['price'] for item in data if item['price'] is not None]
#         bot.send_message(listPrice)
#     elif call.data == "min":
#         msglow = bot.send_message(call.message.chat.id, 'Введите минимальную стоимость:')
#         url = "http://makeup-api.herokuapp.com/api/v1/products.json?price_greater_than={}".format(msglow)
#         response = requests.get(url)
#         data = response.json()
#         listPrice = [item['price'] for item in data if item['price'] is not None]
#         bot.send_message(listPrice)
#     elif call.data == "max":
#         msghigh = bot.send_message(call.message.chat.id, 'Введите максимальную стоимость:')
#         url = "http://makeup-api.herokuapp.com/api/v1/products.json?price_less_than={}".format(msghigh)
#         response = requests.get(url)
#         data = response.json()
#         listPrice = [item['price'] for item in data if item['price'] is not None]
#         bot.send_message(listPrice)




