from loguru import logger
from telebot import types


from database.models import Favorite
from handlers.default_handlers.exception_handler import exc_handler
from loader import bot


@bot.callback_query_handler(func=lambda call: call.data in ["favorite"])
@exc_handler
def favorite_command_handler(call: types.CallbackQuery) -> None:
    """Обработчик, срабатываемый на нажитие клавиши favorite"""

    user_id = call.from_user.id
    chat_id = call.message.chat.id

    with bot.retrieve_data(user_id=user_id, chat_id=chat_id) as data:
        search_cond = data["search_cond"]
        user_choice = data["params"][search_cond]


        if search_cond == "brand":
            Favorite(user_id=user_id, brand=user_choice).save()
        elif search_cond == "product_tag":
            Favorite(user_id=user_id, product_tag=user_choice).save()
        elif search_cond == "product_type":
            Favorite(user_id=user_id, product_type=user_choice).save()

        logger.info(f"The user {user_id} added to favorites: {search_cond}: {user_choice}")

        bot.send_message(chat_id=chat_id, text=f"{search_cond}: {user_choice}")

