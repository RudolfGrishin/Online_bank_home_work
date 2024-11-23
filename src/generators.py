from typing import List, Dict, Any, Iterator


# Реализация функции "filter_by_currency".
def filter_by_currency(transactions: List[Dict[str, Any]], currency: str) -> Iterator[Dict[str, Any]]:
    """Фильтрует транзакции по заданной валюте."""

    for transaction in transactions:
        if transaction.get("currency") == currency:
            yield transaction


# Пример использования
transactions = [
    {"id": 1, "amount": 100, "currency": "USD"},
    {"id": 2, "amount": 200, "currency": "EUR"},
    {"id": 3, "amount": 150, "currency": "USD"},
]

# Итерация по транзакциям в долларах
for transaction in filter_by_currency(transactions, "USD"):
    print(transaction)


# Реализация функции "transaction_descriptions".
def transaction_descriptions(transactions: List[Dict[str, Any]]) -> Iterator[str]:
    """Генератор, который возвращает описание каждой транзакции."""

    for transaction in transactions:
        transaction_id = transaction.get("id")
        amount = transaction.get("amount")
        currency = transaction.get("currency")

        description = f"Transaction ID: {transaction_id}, " f"Amount: {amount} {currency}"
        yield description


# Пример использования
transactions = [
    {"id": 1, "amount": 100, "currency": "USD"},
    {"id": 2, "amount": 200, "currency": "EUR"},
    {"id": 3, "amount": 150, "currency": "USD"},
]

# Итерация по описаниям транзакций
for description in transaction_descriptions(transactions):
    print(description)


# Реализация функции "card_number_generator".
def card_number_generator(start: int, end: int) -> Iterator[str]:
    """Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX."""

    for number in range(start, end + 1):
        formatted_number = f"{number:016d}"
        yield f"{formatted_number[:4]} {formatted_number[4:8]} {formatted_number[8:12]} {formatted_number[12:16]}"


# Пример использования
start_value = 1
end_value = 10

# Итерация по сгенерированным номерам карт
for card_number in card_number_generator(start_value, end_value):
    print(card_number)
