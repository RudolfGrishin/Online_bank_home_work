import os
import unittest
from unittest.mock import patch, MagicMock
from typing import Dict, Union, Optional
import requests


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


class TestConvertTransactionToRub(unittest.TestCase):

    @patch("os.getenv")
    @patch("requests.get")
    def test_convert_usd_to_rub(self, mock_get: MagicMock, mock_getenv: MagicMock) -> None:
        mock_getenv.return_value = "dummy_api_key"
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"result": 7500.0}
        mock_get.return_value = mock_response

        transaction: Dict[str, Union[str, float]] = {"amount": 100.0, "currency": "USD"}
        result = convert_transaction_to_rub(transaction)
        self.assertEqual(result, 7500.0)

    @patch("os.getenv")
    @patch("requests.get")
    def test_invalid_currency(self, mock_get: MagicMock, mock_getenv: MagicMock) -> None:
        transaction: Dict[str, Union[str, float]] = {"amount": 100.0, "currency": "JPY"}
        with self.assertRaises(ValueError) as context:
            convert_transaction_to_rub(transaction)
        self.assertEqual(str(context.exception), "Валюта JPY не поддерживается.")

    @patch("os.getenv")
    @patch("requests.get")
    def test_no_api_key(self, mock_get: MagicMock, mock_getenv: MagicMock) -> None:
        mock_getenv.return_value = None
        transaction: Dict[str, Union[str, float]] = {"amount": 100.0, "currency": "USD"}
        with self.assertRaises(ValueError) as context:
            convert_transaction_to_rub(transaction)
        self.assertEqual(str(context.exception), "Ключ API не найден в переменных окружения.")

    @patch("os.getenv")
    @patch("requests.get")
    def test_api_error(self, mock_get: MagicMock, mock_getenv: MagicMock) -> None:
        mock_getenv.return_value = "dummy_api_key"
        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_response.text = "Internal Server Error"
        mock_get.return_value = mock_response

        transaction: Dict[str, Union[str, float]] = {"amount": 100.0, "currency": "USD"}
        with self.assertRaises(ValueError) as context:
            convert_transaction_to_rub(transaction)
        self.assertEqual(str(context.exception), "Ошибка при получении данных с API: 500 - Internal Server Error")

    @patch("os.getenv")
    @patch("requests.get")
    def test_result_key_not_in_response(self, mock_get: MagicMock, mock_getenv: MagicMock) -> None:
        mock_getenv.return_value = "dummy_api_key"
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {}
        mock_get.return_value = mock_response

        transaction: Dict[str, Union[str, float]] = {"amount": 100.0, "currency": "USD"}
        with self.assertRaises(ValueError) as context:
            convert_transaction_to_rub(transaction)
        self.assertEqual(str(context.exception), "Ключ 'result' отсутствует в ответе API.")

    @patch("os.getenv")
    def test_convert_rub(self, mock_getenv: MagicMock) -> None:
        transaction: Dict[str, Union[str, float]] = {"amount": 100.0, "currency": "RUB"}
        result = convert_transaction_to_rub(transaction)
        self.assertEqual(result, 100.0)


if __name__ == "__main__":
    unittest.main()
