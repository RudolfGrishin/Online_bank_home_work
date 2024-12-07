import json
import os
from typing import List, Dict, Any, Union


def load_transactions(file_path: str) -> List[Dict[str, Any]]:
    """Загружает финансовые транзакции из указанного JSON-файла."""

    # Проверяем, существует ли файл
    if not os.path.isfile(file_path):
        return []

    # Пытаемся открыть и загрузить данные из файла
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data: Union[List[Dict[str, Any]], Any] = json.load(file)
            # Проверяем, является ли загруженные данные списком
            if isinstance(data, list):
                return data
            else:
                return []
    except (json.JSONDecodeError, IOError):
        # Если произошла ошибка при чтении или парсинге JSON, возвращаем пустой список
        return []


# Пример использования функции
if __name__ == "__main__":
    # Указываем путь к файлу operations.json
    transactions_file_path = os.path.join("Data", "operations.json")
    transactions = load_transactions(transactions_file_path)
    print("Загруженные транзакции:", transactions)
