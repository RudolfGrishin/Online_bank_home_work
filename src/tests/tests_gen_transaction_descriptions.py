import pytest
from typing import List, Dict, Any, Iterator, Tuple


# Функция для генерации описаний транзакций
def transaction_descriptions(transactions: List[Dict[str, Any]]) -> Iterator[str]:
    """Генератор, который возвращает описание каждой транзакции."""
    for transaction in transactions:
        description = f"Transaction ID: {transaction.get('id')}, Amount: {transaction.get('amount')} {transaction.get('currency')}"
        yield description


# Фикстура для тестовых данных
@pytest.fixture
def transaction_test_data() -> List[Tuple[List[Dict[str, Any]], List[str]]]:
    """Фикстура для тестовых данных, возвращает параметры для теста."""
    return [
        (
            [
                {"id": 1, "amount": 100, "currency": "USD"},
                {"id": 2, "amount": 200, "currency": "EUR"},
                {"id": 3, "amount": 150, "currency": "USD"},
            ],
            [
                "Transaction ID: 1, Amount: 100 USD",
                "Transaction ID: 2, Amount: 200 EUR",
                "Transaction ID: 3, Amount: 150 USD",
            ],
        ),
        ([{"id": 4, "amount": 300, "currency": "JPY"}], ["Transaction ID: 4, Amount: 300 JPY"]),
        ([], []),
        (
            [
                {"id": 5, "amount": 400},
                {"id": 6, "amount": 500, "currency": None},
            ],
            [
                "Transaction ID: 5, Amount: 400 None",
                "Transaction ID: 6, Amount: 500 None",
            ],
        ),
    ]


# Параметризованный тест
@pytest.mark.parametrize(
    "transactions, expected_descriptions",
    [
        (
            [
                {"id": 1, "amount": 100, "currency": "USD"},
                {"id": 2, "amount": 200, "currency": "EUR"},
                {"id": 3, "amount": 150, "currency": "USD"},
            ],
            [
                "Transaction ID: 1, Amount: 100 USD",
                "Transaction ID: 2, Amount: 200 EUR",
                "Transaction ID: 3, Amount: 150 USD",
            ],
        ),
        ([{"id": 4, "amount": 300, "currency": "JPY"}], ["Transaction ID: 4, Amount: 300 JPY"]),
        ([], []),
        (
            [
                {"id": 5, "amount": 400},
                {"id": 6, "amount": 500, "currency": None},
            ],
            [
                "Transaction ID: 5, Amount: 400 None",
                "Transaction ID: 6, Amount: 500 None",
            ],
        ),
    ],
)
def test_transaction_descriptions(transactions: List[Dict[str, Any]], expected_descriptions: List[str]) -> None:
    result = list(transaction_descriptions(transactions))
    assert result == expected_descriptions
