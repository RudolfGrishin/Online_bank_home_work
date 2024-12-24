from typing import List, Dict


def count_transactions_by_category(transactions: List[Dict[str, str]], categories: List[str]) -> Dict[str, int]:
    """Подсчитывает количество операций в каждой категории."""

    # Инициализация словаря для подсчета операций по категориям
    category_count: Dict[str, int] = {category: 0 for category in categories}

    # Проход по каждой транзакции
    for transaction in transactions:
        description: str = transaction.get("description", "")
        # Проверка каждой категории в описании транзакции
        for category in categories:
            if category.lower() in description.lower():
                category_count[category] += 1

    return category_count


# Пример использования функции
if __name__ == "__main__":
    # Пример списка транзакций
    transactions: List[Dict[str, str]] = [
        {"description": "Открытие вклада", "amount": "40542", "currency": "RUB"},
        {"description": "Перевод с карты на карту", "amount": "130", "currency": "USD"},
        {"description": "Перевод организации", "amount": "8390", "currency": "RUB"},
        {"description": "Перевод со счета на счет", "amount": "8200", "currency": "EUR"},
        {"description": "Оплата услуг", "amount": "1500", "currency": "RUB"},
    ]

    categories: List[str] = ["Перевод", "Открытие", "Оплата"]
    result: Dict[str, int] = count_transactions_by_category(transactions, categories)

    print("Количество операций по категориям:")
    for category, count in result.items():
        print(f"{category}: {count}")
