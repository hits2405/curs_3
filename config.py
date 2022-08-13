import os

# пути к файлам и настройки

DATA_PATH_POST = os.path.join("data", 'posts.json')  # путь к постам
DATA_PATH_COMMENT = os.path.join("data", "comments.json")  # путь к комментариям
DATA_PATH_BOOKSMARKS = os.path.join("data", "bookmarks.json")  # путь к лайкам
LOGGER_API_PATH = os.path.join("logs", "api.log")  # путь к логам
LOGGER_FORMAT = f"%(pastime)s - [%(levelness)s] -  %(name)s - " \
                f"(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"  # путь к формату логов
