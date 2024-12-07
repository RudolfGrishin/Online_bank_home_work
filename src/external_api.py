import os
import requests
from dotenv import load_dotenv
from typing import Dict, Union, Optional

# Загружаем переменные окружения из файла .env
load_dotenv()

# Определяем типы для удобства
AmountDict = Dict[str, Union[float, Dict[str, str]]]


def convert_transaction_to_rub(transaction: Dict[str, AmountDict]) -> float:
    """ Конвертирует сумму транзакции в рубли. """

    # Извлекаем вложенный словарь operationAmount
    operation_amount = transaction.get("operationAmount")

    if not isinstance(operation_amount, dict):
        raise ValueError("operationAmount должен быть словарем.")

    # Извлекаем сумму и валюту
    amount_value = operation_amount.get("amount")

    if not isinstance(amount_value, (float, int)):  # Проверяем, что это число
        raise ValueError("Сумма транзакции должна быть числом.")

    currency_info = operation_amount.get("currency")

    if not isinstance(currency_info, dict):
        raise ValueError("currency должен быть словарем.")

    currency: Optional[str] = currency_info.get("code")

    if currency not in ["RUB", "USD", "EUR"]:
        raise ValueError(f"Валюта {currency} не поддерживается.")

    if amount_value is None:
        raise ValueError("Сумма транзакции не может быть None.")

    if currency == "RUB":
        return float(amount_value)  # Если валюта уже в рублях, просто возвращаем сумму

    # Получаем ключ API из переменной окружения
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("Ключ API не найден в переменных окружения.")

    # Формируем URL для API
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount_value}"

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
transaction_example: Dict[str, AmountDict] = {"operationAmount": {"amount": 100.0, "currency": {"code": "USD"}}}

try:
    result = convert_transaction_to_rub(transaction_example)
    print(f"Сумма транзакции в рублях: {result:.2f}")
except ValueError as e:
    print(e)
