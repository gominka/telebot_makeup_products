import datetime

from telebot.handler_backends import State, StatesGroup
from telebot.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config_data.config import DATE_FORMAT
from database.models import Conditions
from loader import bot


class UserState(StatesGroup):
    brand = State()
    new_task_title = State()
    new_find_title = State()
    new_task_due_date = State()
    tasks_make_done = State()
    condition_selection = State()


@bot.message_handler(state=UserState.brand)
def brand_condition(message: Message) -> None:
    print("1")
    markup = InlineKeyboardMarkup(row_width=1)
    list_brand = InlineKeyboardButton(text='Поиск товаров по бренду',
                                      callback_data="")
    brand_search = InlineKeyboardButton(text='Переход на сайт бренда',
                                        callback_data='brand_search')
    markup.add(list_brand, brand_search)
    bot.send_message(message.chat.id,
                     "Выберете опцию: ",
                     reply_markup=markup)


@bot.message_handler(state=UserState.new_find_title)
def process_task_title(message: Message) -> None:
    with bot.retrieve_data(message.from_user.id) as data:
        data["new_task"]["title"] = message.text
    bot.send_message(message.from_user.id, "Введите дату (ДД.ММ.ГГГГ):")
    bot.set_state(message.from_user.id, UserState.new_task_due_date)


@bot.message_handler(state=UserState.new_task_due_date)
def process_task_due_date(message: Message) -> None:
    due_date_string = message.text
    try:
        due_date = datetime.datetime.strptime(due_date_string, DATE_FORMAT)
    except ValueError:
        bot.send_message(message.from_user.id, "Введите дату (ДД.ММ.ГГГГ):")
        return

    with bot.retrieve_data(message.from_user.id) as data:
        data["new_task"]["due_date"] = due_date

    new_task = Conditions(**data["new_task"])
    new_task.save()
    bot.send_message(message.from_user.id, f"Задача добавлена:\n{new_task}")
    bot.delete_state(message.from_user.id)


@bot.message_handler(state=UserState.tasks_make_done)
def process_task_done(message: Message) -> None:
    task_id = int(message.text)
    task = Conditions.get_or_none(Conditions.task_id == task_id)
    if task is None:
        bot.send_message(message.from_user.id, "Задачи с таким ID не существует.")
        return

    if task.telegram_id != message.from_user.id:
        bot.send_message(
            message.from_user.id, "Вы не являетесь владельцем данной задачи."
        )
        return

    task.is_done = not task.is_done
    task.save()
    bot.send_message(message.from_user.id, task)


@bot.message_handler(state=UserState.new_task_title)
def process_task_title(message: Message) -> None:
    with bot.retrieve_data(message.from_user.id) as data:
        data["new_task"]["title"] = message.text
    bot.send_message(message.from_user.id, "Введите дату (ДД.ММ.ГГГГ):")
    bot.set_state(message.from_user.id, UserState.new_task_due_date)


@bot.message_handler(state=UserState.new_task_due_date)
def process_task_due_date(message: Message) -> None:
    due_date_string = message.text
    try:
        due_date = datetime.datetime.strptime(due_date_string, DATE_FORMAT)
    except ValueError:
        bot.send_message(message.from_user.id, "Введите дату (ДД.ММ.ГГГГ):")
        return

    with bot.retrieve_data(message.from_user.id) as data:
        data["new_task"]["due_date"] = due_date

    new_task = Conditions(**data["new_task"])
    new_task.save()
    bot.send_message(message.from_user.id, f"Задача добавлена:\n{new_task}")
    bot.delete_state(message.from_user.id)


@bot.message_handler(state=UserState.tasks_make_done)
def process_task_done(message: Message) -> None:
    task_id = int(message.text)
    task = Conditions.get_or_none(Conditions.task_id == task_id)
    if task is None:
        bot.send_message(message.from_user.id, "Задачи с таким ID не существует.")
        return

    if Conditions.user_id != message.from_user.id:
        bot.send_message(
            message.from_user.id, "Вы не являетесь владельцем данной задачи."
        )
        return

    task.is_done = not task.is_done
    task.save()
    bot.send_message(message.from_user.id, task)
