START = "Добро пожаловать в наш бот для поиска товаров!" \
        "\n\n Выберите условие для начала поиска: " \
        "\n\n {} /brand - Выбрать бренд"\
        "\n\n {} /product_tag - Выбрать тэг" \
       "\n\n {} /product_type - Выбрать тип" \
       "\n\n {} /name - Поиск по имени"


HELP = "Список доступных команд:"\
       "\n\n {} /brand - Выбрать бренд"\
       "\n\n {} /product_tag - Выбрать тэг" \
       "\n\n {} /product_type - Выбрать тип" \
       "\n\n {} /name - Поиск по имени"

COND = "Выберите команду для поиска:\n\n"\
       "{} /brand - Выбрать бренд"\
       "{} /product_tag - Выбрать тэг" \
       "{} /product_type - Выбрать тип" \
       "{} /name - Поиск по имени"\
       "\n\n {} /highprice - Установить максимальную цену"\
       "{} /lowprice - Установить минимальную цену"\
       "{} /highrating - Узнать топ товаров с высоким рейтингом"\
       "{} /lowrating - Узнать топ товаров с низким рейтингом"\
       "\n\n {} /add - Добавить в избранное"\
       "\n\n {} /favourite - Узнать добавление в избранное"



USER_HANDLER = "Что будем искать? "\
               "\n\n Напиши условие поиска."

START_OVER = "Начать поиск заново"


IS_NOT_NUMBER = "Age should be a positive number, try again."

SHOW_DATA = "First name: {}\nLast name: {}\nAge: {}"

DATA_IS_SAVED = "Your data is saved!\n" + SHOW_DATA
ALREADY_REGISTERED = "You are already registered!\n" + SHOW_DATA
SHOW_DATA_WITH_PREFIX = "Your data:\n" + SHOW_DATA

NOT_REGISTERED = "You are not registered yet, try /register."

CANCEL_REGISTER = "Cancelled! Your data is not saved."

DELETE_ACCOUNT = "Are you sure you want to delete your account?"
DELETE_ACCOUNT_OPTIONS = {"Yes!": True, "No..": False}
DELETE_ACCOUNT_UNKNOWN = "I don't understand this command."
DELETE_ACCOUNT_DONE = "Done! You can /register again."
DELETE_ACCOUNT_CANCEL = "Ok, stay for longer!"