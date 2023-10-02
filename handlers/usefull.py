#bot.answer_callback_query(callback_query_id=call.id, text='Hello world')
# import telebot
#
# token = ''
# file_path = ''
# client_status = {}
# bot = telebot.TeleBot(token)
#
# def save(data):
#     with open(file_path, 'a') as log_file:
#         log_file.write(data)
#
# @bot.message_handler(commands=['begin'])
# def begin(message):
#     client_id = message.from_user.id
#     client_status[client_id] = 'wait_for_data'
#     bot.send_message(chat_id=client_id, text='Enter data: ')
#
# @bot.message_handler(content_types=['text'])
# def handler(message):
#     client_id = message.from_user.id
#     if client_id in client_status and client_status[client_id] == 'wait_for_data':
#         save(message.text) # сохраняем данные
#         bot.send_message(chat_id=client_id, text='Done.')
#         del client_status[client_id]
#
# if __name__ == '__main__':
#     bot.polling(none_stop=True)