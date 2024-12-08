import os
import json
import logging
from typing import List, Dict, Any, Union

# Путь к файлу логов (в корне проекта)
log_file_path = os.path.join("..", "logs", "utils.log")  # Путь к логам из папки src
print(f"Логи будут записываться в: {os.path.abspath(log_file_path)}")

# Создание отдельного логгера для модуля utils
logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)  # Установлен уровень логирования не меньше, чем DEBUG

# Настройка обработчика для логера модуля utils
file_handler = logging.FileHandler(log_file_path, mode="w", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)

# Настройка форматировщика для логера модуля utils
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)

# Добавление обработчика к логгеру модуля utils
logger.addHandler(file_handler)


def load_transactions(file_path: str) -> List[Dict[str, Any]]:
    """Загружает финансовые транзакции из указанного JSON-файла."""

    # Проверяем, существует ли файл
    if not os.path.isfile(file_path):
        logger.error(f"Ошибка: Файл '{file_path}' не найден.")  # Логирование ошибки
        return []

    # Пытаемся открыть и загрузить данные из файла
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data: Union[List[Dict[str, Any]], Any] = json.load(file)

            # Проверяем, является ли загруженные данные списком
            if isinstance(data, list):
                logger.info("Успешно загружены транзакции из файла.")  # Логирование успешного случая
                return data
            else:
                logger.error("Ошибка: Загруженные данные не являются списком.")  # Логирование ошибки
                return []
    except FileNotFoundError:
        logger.error(f"Ошибка: Файл '{file_path}' не найден.")  # Логирование ошибки
        return []
    except json.JSONDecodeError:
        logger.error(f"Ошибка: Не удалось декодировать JSON из файла '{file_path}'.")  # Логирование ошибки
        return []
    except IOError:
        logger.error(f"Ошибка: Не удалось прочитать файл '{file_path}'.")  # Логирование ошибки
        return []


if __name__ == "__main__":
    """
    Пример использования функции load_transactions для загрузки транзакций
    из файла operations.json и их вывода на экран.
    """
    # Указываем путь к файлу operations.json (предполагается, что он находится в папке src/Data)
    transactions_file_path: str = os.path.join("Data", "operations.json")
    transactions: List[Dict[str, Any]] = load_transactions(transactions_file_path)
    print("Загруженные транзакции:", transactions)


# import json
# import os
# from typing import List, Dict, Any, Union


# def load_transactions(file_path: str) -> List[Dict[str, Any]]:
#    """ Загружает финансовые транзакции из указанного JSON-файла. """

# Проверяем, существует ли файл
#    if not os.path.isfile(file_path):
#        print(f"Ошибка: Файл '{file_path}' не найден.")
#        return []

# Пытаемся открыть и загрузить данные из файла
#    try:
#        with open(file_path, "r", encoding="utf-8") as file:
#            data: Union[List[Dict[str, Any]], Any] = json.load(file)
# Проверяем, является ли загруженные данные списком
#            if isinstance(data, list):
#                return data
#            else:
#                print("Ошибка: Загруженные данные не являются списком.")
#                return []
#    except FileNotFoundError:
#        print(f"Ошибка: Файл '{file_path}' не найден.")
#        return []
#    except json.JSONDecodeError:
#        print(f"Ошибка: Не удалось декодировать JSON из файла '{file_path}'.")
#        return []
#    except IOError:
#        print(f"Ошибка: Не удалось прочитать файл '{file_path}'.")
#        return []


# if __name__ == "__main__":
#    """
#    Пример использования функции load_transactions для загрузки транзакций
#    из файла operations.json и их вывода на экран.
#    """
# Указываем путь к файлу operations.json
#    transactions_file_path: str = os.path.join("Data", "operations.json")
#    transactions: List[Dict[str, Any]] = load_transactions(transactions_file_path)
#    print("Загруженные транзакции:", transactions)
