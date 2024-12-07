import json
import os
import unittest
from unittest.mock import mock_open, patch, MagicMock
from typing import List, Dict, Any, Union


# Импортируем вашу функцию
def load_transactions(file_path: str) -> List[Dict[str, Any]]:
    """Загружает финансовые транзакции из указанного JSON-файла."""

    if not os.path.isfile(file_path):
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data: Union[List[Dict[str, Any]], Any] = json.load(file)
            if isinstance(data, list):
                return data
            else:
                return []
    except (json.JSONDecodeError, IOError):
        return []


class TestLoadTransactions(unittest.TestCase):

    @patch("os.path.isfile")
    def test_file_does_not_exist(self, mock_isfile: MagicMock) -> None:
        mock_isfile.return_value = False
        result = load_transactions("non_existent_file.json")
        self.assertEqual(result, [])

    @patch("os.path.isfile")
    @patch("builtins.open", new_callable=mock_open)
    def test_file_contains_invalid_json(self, mock_file: MagicMock, mock_isfile: MagicMock) -> None:
        mock_isfile.return_value = True
        mock_file.side_effect = IOError("File not accessible")
        result = load_transactions("invalid_file.json")
        self.assertEqual(result, [])

    @patch("os.path.isfile")
    @patch("builtins.open", new_callable=mock_open, read_data='[{"amount": 100, "currency": "USD"}]')
    def test_file_contains_valid_json(self, mock_file: MagicMock, mock_isfile: MagicMock) -> None:
        mock_isfile.return_value = True
        result = load_transactions("valid_file.json")
        expected = [{"amount": 100, "currency": "USD"}]
        self.assertEqual(result, expected)

    @patch("os.path.isfile")
    @patch("builtins.open", new_callable=mock_open, read_data='{"amount": 100, "currency": "USD"}')
    def test_file_contains_non_list_json(self, mock_file: MagicMock, mock_isfile: MagicMock) -> None:
        mock_isfile.return_value = True
        result = load_transactions("non_list_file.json")
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
