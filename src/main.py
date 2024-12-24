import json
from typing import List, Dict, Any
from file_reader import read_transactions_from_csv, read_transactions_from_excel
from external_api import convert_transaction_to_rub


def main() -> None:
    """Основная функция программы, связывающая функциональности."""
    print("Программа: Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Пользователь: ")

    transactions: List[Dict[str, Any]] = []

    if choice == "1":
        file_path = "C:/Users/newuser/PycharmProjects/online_bank_projects/Data/operations.json"
        print("Программа: Для обработки выбран JSON-файл.")
        with open(file_path, "r", encoding="utf-8") as f:
            transactions = json.load(f)
    elif choice == "2":
        file_path = "Data/transactions.csv"
        print("Программа: Для обработки выбран CSV-файл.")
        transactions = read_transactions_from_csv(file_path)
    elif choice == "3":
        file_path = "Data/transactions_excel.xlsx"
        print("Программа: Для обработки выбран XLSX-файл.")
        transactions = read_transactions_from_excel(file_path)
    else:
        print("Программа: Неверный выбор.")
        return

    while True:
        status = input(
            "Программа: Введите статус, по которому необходимо выполнить фильтрацию. "
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\nПользователь: "
        )
        if status.lower() in ["executed", "canceled", "pending"]:
            break
        else:
            print(f'Программа: Статус операции "{status}" недоступен.')

    # Используем .get() для безопасного доступа к ключу 'state'
    filtered_transactions = [t for t in transactions if t.get("state", "").lower() == status.lower()]
    print(f'Программа: Операции отфильтрованы по статусу "{status.upper()}".')

    # Сортировка
    sort_choice = input("Программа: Отсортировать операции по дате? Да/Нет\nПользователь: ").strip().lower()
    if sort_choice == "да":
        order_choice = (
            input("Программа: Отсортировать по возрастанию или по убыванию?\nПользователь: ").strip().lower()
        )
        ascending = order_choice == "по возрастанию"
        filtered_transactions.sort(key=lambda x: x["date"], reverse=not ascending)

    # Фильтрация по валюте
    currency_choice = input("Программа: Выводить только рублевые транзакции? Да/Нет\nПользователь: ").strip().lower()
    if currency_choice == "да":
        filtered_transactions = [t for t in filtered_transactions if t["operationAmount"]["currency"]["code"] == "RUB"]

    # Фильтрация по описанию
    description_choice = (
        input("Программа: Отфильтровать список транзакций по определенному слову в описании? Да/Нет\nПользователь: ")
        .strip()
        .lower()
    )
    if description_choice == "да":
        keyword = input("Введите слово для фильтрации по описанию:\nПользователь: ")
        filtered_transactions = [t for t in filtered_transactions if keyword.lower() in t["description"].lower()]

    # Вывод результатов
    if filtered_transactions:
        print("Программа: Распечатываю итоговый список транзакций...")
        print(f"Всего банковских операций в выборке: {len(filtered_transactions)}")
        for transaction in filtered_transactions:
            # Проверяем и обрабатываем данные перед вызовом функции
            try:
                operation_amount = transaction.get("operationAmount")

                if not isinstance(operation_amount, dict):
                    raise ValueError("operationAmount должен быть словарем.")

                amount_value = operation_amount.get("amount")

                if amount_value is None:
                    raise ValueError("Сумма транзакции не может быть None.")

                # Преобразовываем amount_value в float, если это строка
                if isinstance(amount_value, str):
                    try:
                        amount_value = float(amount_value)
                    except ValueError:
                        raise ValueError("Сумма транзакции должна быть числом.")

                elif not isinstance(amount_value, (float, int)):
                    raise ValueError("Сумма транзакции должна быть числом.")

                # Проверяем currency
                currency_info = operation_amount.get("currency")
                if not isinstance(currency_info, dict):
                    raise ValueError("currency должен быть словарем.")

                currency_code = currency_info.get("code")
                if currency_code not in ["RUB", "USD", "EUR"]:
                    raise ValueError(f"Валюта {currency_code} не поддерживается.")

                # все проверки пройдены, вызываем функцию
                amount_in_rub = convert_transaction_to_rub(transaction)

                print(f"{transaction['date']} {transaction['description']}")
                # Обработка наличия или отсутствия ключа 'from'
                from_account = transaction.get("from", "N/A")
                print(f"Счет **{from_account[-4:] if from_account != 'N/A' else 'N/A'}")
                print(f"Сумма: {amount_in_rub:.2f} {transaction['operationAmount']['currency']['name']}\n")

            except ValueError as e:
                print(f"Ошибка при обработке транзакции: {e}")

    else:
        print("Программа: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")


if __name__ == "__main__":
    main()
