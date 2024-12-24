import re
from typing import List, Dict


def search_transactions(transactions: List[Dict[str, str]], search_string: str) -> List[Dict[str, str]]:
    """Ищет транзакции в списке по заданной строке в описании."""

    # Преобразуем строку поиска в регулярное выражение
    pattern = re.compile(re.escape(search_string), re.IGNORECASE)

    # Фильтруем транзакции по описанию
    matched_transactions = [
        transaction for transaction in transactions if pattern.search(transaction.get("description", ""))
    ]

    return matched_transactions


# Пример использования функции
if __name__ == "__main__":
    # Пример списка транзакций
    transactions: List[Dict[str, str]] = [
        {"description": "Открытие вклада", "amount": "40542", "currency": "RUB"},
        {"description": "Перевод с карты на карту", "amount": "130", "currency": "USD"},
        {"description": "Перевод организации", "amount": "8390", "currency": "RUB"},
        {"description": "Перевод со счета на счет", "amount": "8200", "currency": "EUR"},
    ]

    search_string: str = "перевод"
    result: List[Dict[str, str]] = search_transactions(transactions, search_string)

    print("Найденные транзакции:")
    for transaction in result:
        print(transaction)
