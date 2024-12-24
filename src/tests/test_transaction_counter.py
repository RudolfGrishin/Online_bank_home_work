import pytest
from typing import List, Dict
from src.transaction_counter import count_transactions_by_category


# Тесты
def test_count_transactions_by_category() -> None:
    """Тестирует функцию count_transactions_by_category."""

    # Пример списка транзакций
    transactions: List[Dict[str, str]] = [
        {"description": "Открытие вклада", "amount": "40542", "currency": "RUB"},
        {"description": "Перевод с карты на карту", "amount": "130", "currency": "USD"},
        {"description": "Перевод организации", "amount": "8390", "currency": "RUB"},
        {"description": "Перевод со счета на счет", "amount": "8200", "currency": "EUR"},
        {"description": "Оплата услуг", "amount": "1500", "currency": "RUB"},
    ]

    categories: List[str] = ["Перевод", "Открытие", "Оплата"]

    # Тест 1: Проверка правильного подсчета
    expected_result: Dict[str, int] = {"Перевод": 3, "Открытие": 1, "Оплата": 1}
    assert count_transactions_by_category(transactions, categories) == expected_result

    # Тест 2: Проверка на отсутствие совпадений
    categories_no_match: List[str] = ["Депозит", "Кредит"]
    expected_result_no_match: Dict[str, int] = {"Депозит": 0, "Кредит": 0}
    assert count_transactions_by_category(transactions, categories_no_match) == expected_result_no_match

    # Тест 3: Проверка регистронезависимого поиска
    categories_case_insensitive: List[str] = ["перевод", "открытие", "оплата"]
    expected_result_case_insensitive: Dict[str, int] = {"перевод": 3, "открытие": 1, "оплата": 1}
    assert (
        count_transactions_by_category(transactions, categories_case_insensitive) == expected_result_case_insensitive
    )

    # Тест 4: Проверка с пустым списком транзакций
    empty_transactions: List[Dict[str, str]] = []
    expected_result_empty: Dict[str, int] = {"Перевод": 0, "Открытие": 0, "Оплата": 0}
    assert count_transactions_by_category(empty_transactions, categories) == expected_result_empty

    # Тест 5: Проверка с пустыми категориями
    expected_result_empty_categories: Dict[str, int] = {}
    assert count_transactions_by_category(transactions, []) == expected_result_empty_categories


# Запуск тестов
if __name__ == "__main__":
    pytest.main()
