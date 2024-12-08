import logging
import json
import os
from typing import Any, Dict, List, Union

# Проверка, что директория для логов существует
log_directory = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

# Настройка логирования
logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)

# Создание обработчика для записи логов в файл
file_handler = logging.FileHandler(os.path.join(log_directory, "utils.log"), encoding="utf-8")
file_handler.setLevel(logging.DEBUG)

# Настройка формата логов
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

# Добавление обработчика к логеру
logger.addHandler(file_handler)


def load_operations(file_path: str) -> List[Dict[str, Any]]:
    """ Загрузка операций из JSON файла. """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data: Union[List[Dict[str, Any]], Any] = json.load(f)  # Явная аннотация типа
            if not isinstance(data, list):
                logger.error("Ошибка: ожидается список операций, но получено: %s", type(data))
                raise ValueError("Ожидается список операций")
            return data
    except FileNotFoundError:
        logger.error("Ошибка: файл '%s' не найден.", file_path)
        raise
    except json.JSONDecodeError as e:
        logger.error("Ошибка при чтении файла '%s': %s", file_path, e)
        raise
    except Exception as e:
        logger.error("Неизвестная ошибка при загрузке файла '%s': %s", file_path, e)
        raise


# Пример использования функции
if __name__ == "__main__":
    try:
        operations = load_operations("Data/operations.json")
    except Exception as e:
        logger.error("Произошла ошибка: %s", e)


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
