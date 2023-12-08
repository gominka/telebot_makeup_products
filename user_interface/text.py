from user_interface import emoji

MAIN_COMMANDS = f"\n\n {emoji.start_condition['brand']} /brand - Select a brand" \
                f"\n\n {emoji.start_condition['product_tag']} /product_tag - Select a tag" \
                f"\n\n {emoji.start_condition['product_type']} /product_type - Select a type"

SEARCH_COMMANDS = f"\n\n{emoji.search_condition['high']} /high - Set a maximum price or rating" \
                  f"\n\n{emoji.search_condition['low']} /low - Set a minimum price or rating"

CUSTOM_COMMANDS = f"\n\n{emoji.addition_condition['favorite']} /favorite - Add to Favorites"\
                  f"\n\n{emoji.addition_condition['start_again']} /start_again - Start over"

FAV_COMMANDS = f"\n\n{emoji.addition_condition['favorite']} /my_favorites - Find out your favorites"


START_MSG = "Welcome to Telegram Bot!" \
            "\n\n Select a condition to start the search: " + MAIN_COMMANDS

HELP_MSG = "List of available commands:" + MAIN_COMMANDS + FAV_COMMANDS

CONDITION = "Select the command:" + MAIN_COMMANDS + SEARCH_COMMANDS + CUSTOM_COMMANDS + FAV_COMMANDS

DESCRIPTION = "Product Description:\n\n" \
              "{}\n" \
              "Product Link:\n\n" \
              "{}"

# USER_HANDLER = "Что будем искать? " \
#                "\n\n Напиши условие поиска."

START_OVER = "Start the search again"
