from telebot.types import CallbackQuery

from database.models import History
from loader import bot


@bot.callback_query_handler(func=lambda call: call.data in ["brands_history", "types_history", "tags_history",
                                                            "products_history", "all_history"])
def history_command_callback(call: CallbackQuery) -> None:
    """

    :param call: CallbackQuery
    :return: None
    """

    user_id = call.from_user.id
    if call.data == "brands_history":
        try:
            sql_select_query = History.select(History.brand_cond).where(History.user_id == user_id)
            result = []
            for row in sql_select_query:
                result.append(str(row))
            bot.reply_to(call.message, "{}".format(set(result)))
        except TypeError:
            bot.reply_to(call.message, "История отсутствует")

    elif call.data == "types_history":
        try:
            sql_select_query = History.select(History.product_type).where(History.user_id == user_id)
            result = []
            for row in sql_select_query:
                result.append(str(row))
            bot.reply_to(call.message, "{}".format(set(result)))

        except TypeError:
            bot.reply_to(call.message, "История отсутствует")

    elif call.data == "tags_history":
        try:
            sql_select_query = History.select(History.tag).where(History.user_id == user_id)
            result = []
            for row in sql_select_query:
                result.append(str(row))
            bot.reply_to(call.message, "{}".format(set(result)))
        except TypeError:
            bot.reply_to(call.message, "История отсутствует")

