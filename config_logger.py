import logging


# настройки логов

def config(app):
    api_logger = logging.getLogger("api_logger")  # название
    api_logger.setLevel(logging.DEBUG)  # настройка регистратора

    api_logger_handler = logging.FileHandler(filename=app.config["LOGGER_API_PATH"])  # путь конфигурации (хранение
    # файла логов)

    api_logger_handler.setLevel(logging.DEBUG)  # # настройка регистратора
    api_logger.addHandler(api_logger_handler)  # добавление обработчика

    api_logger_format = logging.Formatter(app.config["LOGGER_FORMAT"])  # добавление формата записи логов
    api_logger_handler.setFormatter(api_logger_format)  # путь к формату записи логов
