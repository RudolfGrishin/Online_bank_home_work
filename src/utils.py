import json
import os
from typing import List, Dict, Any, Union


def load_transactions(file_path: str) -> List[Dict[str, Any]]:
    """ Загружает финансовые транзакции из указанного JSON-файла."""

    # Проверяем, существует ли файл
    if not os.path.isfile(file_path):
        print(f"Ошибка: Файл '{file_path}' не найден.")
        return []

    # Пытаемся открыть и загрузить данные из файла
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data: Union[List[Dict[str, Any]], Any] = json.load(file)
            # Проверяем, является ли загруженные данные списком
            if isinstance(data, list):
                return data
            else:
                print("Ошибка: Загруженные данные не являются списком.")
                return []
    except FileNotFoundError:
        print(f"Ошибка: Файл '{file_path}' не найден.")
        return []
    except json.JSONDecodeError:
        print(f"Ошибка: Не удалось декодировать JSON из файла '{file_path}'.")
        return []
    except IOError:
        print(f"Ошибка: Не удалось прочитать файл '{file_path}'.")
        return []


if __name__ == "__main__":
    """ Пример использования функции load_transactions для загрузки транзакций
    из файла operations.json и их вывода на экран."""

    # Указываем путь к файлу operations.json
    transactions_file_path: str = os.path.join("Data", "operations.json")
    transactions: List[Dict[str, Any]] = load_transactions(transactions_file_path)
    print("Загруженные транзакции:", transactions)
