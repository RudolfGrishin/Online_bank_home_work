import pandas as pd
from typing import List, Dict, Any


def read_transactions_from_csv(file_path: str) -> List[Dict[Any, Any]]:
    """Считывает финансовые операции из CSV файла."""

    try:
        df = pd.read_csv(file_path)
        transactions: List[Dict[Any, Any]] = df.to_dict(orient="records")
        return transactions
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
        return []
    except pd.errors.EmptyDataError:
        print(f"Файл {file_path} пуст.")
        return []
    except Exception as e:
        print(f"Ошибка при чтении файла {file_path}: {e}")
        return []


def read_transactions_from_excel(file_path: str) -> List[Dict[Any, Any]]:
    """Считывает финансовые операции из Excel файла."""

    try:
        df = pd.read_excel(file_path)
        transactions: List[Dict[Any, Any]] = df.to_dict(orient="records")
        return transactions
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
        return []
    except ValueError:
        print(f"Ошибка при чтении файла {file_path}. Проверьте формат файла.")
        return []
    except Exception as e:
        print(f"Ошибка при чтении файла {file_path}: {e}")
        return []



if __name__ == "__main__":
    csv_file_path = "Data/transactions.csv"
    excel_file_path = "Data/transactions_excel.xlsx"

    csv_transactions = read_transactions_from_csv(csv_file_path)
    print("Транзакции из CSV:", csv_transactions)

    excel_transactions = read_transactions_from_excel(excel_file_path)
    print("Транзакции из Excel:", excel_transactions)
