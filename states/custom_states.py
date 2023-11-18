from loguru import logger
from telebot.handler_backends import State, StatesGroup
from telebot.types import Message

from database.models import History, User
from keyboards.inline.main_comm_inline_markup import (
    main_commands_inline_markup,
    search_inline_markup,
    failure_inline_markup
)
from loader import bot


class UserState(StatesGroup):
    search_state = State()
    search_in_file = State()
    name = State()


@bot.message_handler(commands=['brand', 'tag', 'product_type'], state=UserState.search_state)
def search_state(message: Message) -> None:
    msg_user = message.text[1:]
    user_id = message.from_user.id
    chat_id = message.chat.id

    if User.get_or_none(User.user_id == user_id) is None:
        bot.reply_to(message, "Вы не зарегистрированы. Напишите /start")
        return

    with bot.retrieve_data(user_id=user_id, chat_id=chat_id) as data:
        data["first_cond"] = msg_user

    bot.send_message(
        chat_id=chat_id,
        text="Выберете условие для продолжения поиска: ",
        reply_markup=main_commands_inline_markup(msg_user)
    )


@bot.message_handler(state=UserState.search_in_file)
def search_in_file(message: Message) -> None:
    msg_user = message.text
    user_id = message.from_user.id
    chat_id = message.chat.id

    with bot.retrieve_data(user_id=user_id, chat_id=chat_id) as data:
        condition = data["first_cond"]

    file_name = f"{condition}.txt"
    in_db = "{}".format(condition)

    with open(file_name) as f:
        if msg_user in f.read():
            if condition == "brand":
                History(user_id=user_id, brand=msg_user).save()
                logger.info('Выбранное условие: ' + msg_user + f' User_id - {user_id}')
                bot.send_message(
                    chat_id=chat_id,
                    text="Выберете опцию: ",
                    reply_markup=search_inline_markup(condition)
                )

        else:
            bot.send_message(
                chat_id=chat_id,
                text="Не можем найти такой бренд.",
                reply_markup=failure_inline_markup(condition)
            )

# @bot.message_handler(state=UserState.brand)
# def brand_condition(message: Message) -> None:
#     markup = InlineKeyboardMarkup(row_width=1)
#     list_brand = InlineKeyboardButton(text='Поиск товаров по бренду',
#                                       callback_data="")
#     brand_search = InlineKeyboardButton(text='Переход на сайт бренда',
#                                         callback_data='brand_search')
#     markup.add(list_brand, brand_search)
#     bot.send_message(message.chat.id,
#                      "Выберете опцию: ",
#                      reply_markup=markup)
# #
#
# @bot.message_handler(state=UserState.new_find_title)
# def process_task_title(message: Message) -> None:
#     with bot.retrieve_data(message.from_user.id) as data:
#         data["new_task"]["title"] = message.text
#     bot.send_message(message.from_user.id, "Введите дату (ДД.ММ.ГГГГ):")
#     bot.set_state(message.from_user.id, UserState.new_task_due_date)
#
#
# @bot.message_handler(state=UserState.new_task_due_date)
# def process_task_due_date(message: Message) -> None:
#     due_date_string = message.text
#     try:
#         due_date = datetime.datetime.strptime(due_date_string, DATE_FORMAT)
#     except ValueError:
#         bot.send_message(message.from_user.id, "Введите дату (ДД.ММ.ГГГГ):")
#         return
#
#     with bot.retrieve_data(message.from_user.id) as data:
#         data["new_task"]["due_date"] = due_date
#
#     new_task = Conditions(**data["new_task"])
#     new_task.save()
#     bot.send_message(message.from_user.id, f"Задача добавлена:\n{new_task}")
#     bot.delete_state(message.from_user.id)
#
#
# @bot.message_handler(state=UserState.tasks_make_done)
# def process_task_done(message: Message) -> None:
#     task_id = int(message.text)
#     task = Conditions.get_or_none(Conditions.task_id == task_id)
#     if task is None:
#         bot.send_message(message.from_user.id, "Задачи с таким ID не существует.")
#         return
#
#     if task.telegram_id != message.from_user.id:
#         bot.send_message(
#             message.from_user.id, "Вы не являетесь владельцем данной задачи."
#         )
#         return
#
#     task.is_done = not task.is_done
#     task.save()
#     bot.send_message(message.from_user.id, task)
#
#
# @bot.message_handler(state=UserState.new_task_title)
# def process_task_title(message: Message) -> None:
#     with bot.retrieve_data(message.from_user.id) as data:
#         data["new_task"]["title"] = message.text
#     bot.send_message(message.from_user.id, "Введите дату (ДД.ММ.ГГГГ):")
#     bot.set_state(message.from_user.id, UserState.new_task_due_date)
#
#
# @bot.message_handler(state=UserState.new_task_due_date)
# def process_task_due_date(message: Message) -> None:
#     due_date_string = message.text
#     try:
#         due_date = datetime.datetime.strptime(due_date_string, DATE_FORMAT)
#     except ValueError:
#         bot.send_message(message.from_user.id, "Введите дату (ДД.ММ.ГГГГ):")
#         return
#
#     with bot.retrieve_data(message.from_user.id) as data:
#         data["new_task"]["due_date"] = due_date
#
#     new_task = Conditions(**data["new_task"])
#     new_task.save()
#     bot.send_message(message.from_user.id, f"Задача добавлена:\n{new_task}")
#     bot.delete_state(message.from_user.id)
#
#
# @bot.message_handler(state=UserState.tasks_make_done)
# def process_task_done(message: Message) -> None:
#     task_id = int(message.text)
#     task = Conditions.get_or_none(Conditions.task_id == task_id)
#     if task is None:
#         bot.send_message(message.from_user.id, "Задачи с таким ID не существует.")
#         return
#
#     if Conditions.user_id != message.from_user.id:
#         bot.send_message(
#             message.from_user.id, "Вы не являетесь владельцем данной задачи."
#         )
#         return
#
#     task.is_done = not task.is_done
#     task.save()
#     bot.send_message(message.from_user.id, task)
