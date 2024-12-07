import os
import requests
from dotenv import load_dotenv
from typing import Dict, Union, Optional

# Загружаем переменные окружения из файла .env
load_dotenv()


def convert_transaction_to_rub(transaction: Dict[str, Union[str, float]]) -> float:
    """Конвертирует сумму транзакции в рубли."""
    amount: Optional[Union[str, float]] = transaction.get("amount")
    currency = transaction.get("currency")

    if currency not in ["RUB", "USD", "EUR"]:
        raise ValueError(f"Валюта {currency} не поддерживается.")

    if currency == "RUB":
        if amount is None:
            raise ValueError("Сумма транзакции не может быть None.")
        return float(amount)  # Если валюта уже в рублях, просто возвращаем сумму

    # Получаем ключ API из переменной окружения
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("Ключ API не найден в переменных окружения.")

    # Формируем URL для API
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"

    headers = {"apikey": api_key}

    # Выполняем запрос к API
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise ValueError(f"Ошибка при получении данных с API: {response.status_code} - {response.text}")

    data = response.json()

    # Проверяем наличие ключа 'result' в ответе
    if "result" not in data:
        raise ValueError("Ключ 'result' отсутствует в ответе API.")

    return float(data["result"])


# Пример использования:
transaction_example: Dict[str, Union[str, float]] = {"amount": 100.0, "currency": "USD"}

try:
    result = convert_transaction_to_rub(transaction_example)
    print(f"Сумма транзакции в рублях: {result:.2f}")
except ValueError as e:
    print(e)
