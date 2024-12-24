import pytest
from typing import List, Dict
from src.transaction_search import search_transactions


@pytest.fixture
def sample_transactions() -> List[Dict[str, str]]:
    """Фикстура для предоставления образца транзакций."""
    return [
        {"description": "Открытие вклада", "amount": "40542", "currency": "RUB"},
        {"description": "Перевод с карты на карту", "amount": "130", "currency": "USD"},
        {"description": "Перевод организации", "amount": "8390", "currency": "RUB"},
        {"description": "Перевод со счета на счет", "amount": "8200", "currency": "EUR"},
    ]


def test_search_transactions_found(sample_transactions: List[Dict[str, str]]) -> None:
    """Тест на поиск транзакций, когда совпадения есть."""
    search_string: str = "перевод"
    result: List[Dict[str, str]] = search_transactions(sample_transactions, search_string)
    assert len(result) == 3
    assert all("перевод" in transaction["description"].lower() for transaction in result)


def test_search_transactions_not_found(sample_transactions: List[Dict[str, str]]) -> None:
    """Тест на поиск транзакций, когда совпадений нет."""
    search_string: str = "не существующая строка"
    result: List[Dict[str, str]] = search_transactions(sample_transactions, search_string)
    assert len(result) == 0


def test_search_transactions_case_insensitive(sample_transactions: List[Dict[str, str]]) -> None:
    """Тест на регистронезависимый поиск."""
    search_string: str = "ПЕРЕВОД"
    result: List[Dict[str, str]] = search_transactions(sample_transactions, search_string)
    assert len(result) == 3


def test_search_transactions_empty_description(sample_transactions: List[Dict[str, str]]) -> None:
    """Тест на транзакции с пустым описанием."""
    transactions_with_empty_description: List[Dict[str, str]] = sample_transactions + [
        {"description": "", "amount": "1000", "currency": "RUB"},
    ]
    search_string: str = "перевод"
    result: List[Dict[str, str]] = search_transactions(transactions_with_empty_description, search_string)
    assert len(result) == 3


def test_search_transactions_empty_list() -> None:
    """Тест на поиск в пустом списке транзакций."""
    result: List[Dict[str, str]] = search_transactions([], "перевод")
    assert len(result) == 0


if __name__ == "__main__":
    pytest.main()
