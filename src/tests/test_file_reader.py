import unittest
from unittest.mock import patch, MagicMock
from src.file_reader import read_transactions_from_csv, read_transactions_from_excel
from typing import List, Dict, Any


class TestFileReader(unittest.TestCase):

    @patch("src.file_reader.pd.read_csv")
    def test_read_transactions_from_csv(self, mock_read_csv: MagicMock) -> None:
        # Настройка mock для возврата тестового DataFrame
        mock_read_csv.return_value = MagicMock(
            to_dict=MagicMock(
                return_value=[
                    {"date": "2023-01-01", "amount": 100, "description": "Test transaction 1"},
                    {"date": "2023-01-02", "amount": 200, "description": "Test transaction 2"},
                ]
            )
        )

        transactions: List[Dict[Any, Any]] = read_transactions_from_csv("dummy_path.csv")

        # Проверка, что возвращенные транзакции соответствуют ожидаемым
        expected_transactions: List[Dict[str, Any]] = [
            {"date": "2023-01-01", "amount": 100, "description": "Test transaction 1"},
            {"date": "2023-01-02", "amount": 200, "description": "Test transaction 2"},
        ]
        self.assertEqual(transactions, expected_transactions)

    @patch("src.file_reader.pd.read_excel")
    def test_read_transactions_from_excel(self, mock_read_excel: MagicMock) -> None:
        # Настройка mock для возврата тестового DataFrame
        mock_read_excel.return_value = MagicMock(
            to_dict=MagicMock(
                return_value=[
                    {"date": "2023-01-01", "amount": 150, "description": "Test transaction A"},
                    {"date": "2023-01-02", "amount": 250, "description": "Test transaction B"},
                ]
            )
        )

        transactions: List[Dict[Any, Any]] = read_transactions_from_excel("dummy_path.xlsx")

        # Проверка, что возвращенные транзакции соответствуют ожидаемым
        expected_transactions: List[Dict[str, Any]] = [
            {"date": "2023-01-01", "amount": 150, "description": "Test transaction A"},
            {"date": "2023-01-02", "amount": 250, "description": "Test transaction B"},
        ]
        self.assertEqual(transactions, expected_transactions)

    @patch("src.file_reader.pd.read_csv")
    def test_read_transactions_from_csv_file_not_found(self, mock_read_csv: MagicMock) -> None:
        # Настройка mock для имитации ошибки FileNotFoundError
        mock_read_csv.side_effect = FileNotFoundError

        transactions: List[Dict[Any, Any]] = read_transactions_from_csv("dummy_path.csv")

        # Проверка, что возвращается пустой список
        self.assertEqual(transactions, [])

    @patch("src.file_reader.pd.read_excel")
    def test_read_transactions_from_excel_file_not_found(self, mock_read_excel: MagicMock) -> None:
        # Настройка mock для имитации ошибки FileNotFoundError
        mock_read_excel.side_effect = FileNotFoundError

        transactions: List[Dict[Any, Any]] = read_transactions_from_excel("dummy_path.xlsx")

        # Проверка, что возвращается пустой список
        self.assertEqual(transactions, [])


if __name__ == "__main__":
    unittest.main()
