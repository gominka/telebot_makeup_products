from telebot.types import CallbackQuery

from database.models import Conditions
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
            sql_select_query = Conditions.select(Conditions.brand_cond).where(Conditions.user_id == user_id)
            result = []
            for row in sql_select_query:
                result.append(str(row))
            bot.reply_to(call.message, "{}".format(set(result)))
        except TypeError:
            bot.reply_to(call.message, "История отсутствует")

    elif call.data == "types_history":
        try:
            sql_select_query = Conditions.select(Conditions.product_type_cond).where(Conditions.user_id == user_id)
            result = []
            for row in sql_select_query:
                result.append(str(row))
            bot.reply_to(call.message, "{}".format(set(result)))

        except TypeError:
            bot.reply_to(call.message, "История отсутствует")

    elif call.data == "tags_history":
        try:
            sql_select_query = Conditions.select(Conditions.tag_cond).where(Conditions.user_id == user_id)
            result = []
            for row in sql_select_query:
                result.append(str(row))
            bot.reply_to(call.message, "{}".format(set(result)))
        except TypeError:
            bot.reply_to(call.message, "История отсутствует")

