import pytest
from typing import List, Dict, Any, Iterator


# Функция для фильтрации транзакций
def filter_by_currency(transactions: List[Dict[str, Any]], currency: str) -> Iterator[Dict[str, Any]]:
    """Фильтрует транзакции по заданной валюте."""
    for transaction in transactions:
        if transaction.get("currency") == currency:
            yield transaction


# Фикстура для тестовых транзакций
@pytest.fixture
def transactions() -> List[Dict[str, Any]]:
    return [
        {"id": 1, "amount": 100, "currency": "USD"},
        {"id": 2, "amount": 200, "currency": "EUR"},
        {"id": 3, "amount": 150, "currency": "USD"},
    ]


# Параметризованный тест
@pytest.mark.parametrize(
    "currency, expected",
    [
        (
            "USD",
            [
                {"id": 1, "amount": 100, "currency": "USD"},
                {"id": 3, "amount": 150, "currency": "USD"},
            ],
        ),
        (
            "EUR",
            [
                {"id": 2, "amount": 200, "currency": "EUR"},
            ],
        ),
        ("GBP", []),  # Ожидаем пустой список
    ],
)
def test_filter_by_currency(transactions: List[Dict[str, Any]], currency: str, expected: List[Dict[str, Any]]) -> None:
    result = list(filter_by_currency(transactions, currency))
    assert result == expected


def test_filter_by_currency_empty_list() -> None:
    result = list(filter_by_currency([], "USD"))
    assert result == []  # Ожидаем пустой список


def test_filter_by_currency_no_matching() -> None:
    transactions_no_match: List[Dict[str, Any]] = [
        {"id": 1, "amount": 100, "currency": "JPY"},
        {"id": 2, "amount": 200, "currency": "AUD"},
    ]
    result = list(filter_by_currency(transactions_no_match, "USD"))
    assert result == []  # Ожидаем пустой список
