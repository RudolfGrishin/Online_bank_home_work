import logging
import os
from typing import Optional

# Настройка логирования
log_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs")
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)

# Создание обработчика для записи логов в файл
file_handler = logging.FileHandler(os.path.join(log_directory, "utils.log"), encoding="utf-8")
file_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def mask_card_number(card_number: str) -> Optional[str]:
    """ Замаскировать номер карты, оставляя только последние 4 цифры видимыми. """
    if not isinstance(card_number, str) or len(card_number) < 4:
        logger.error("Некорректный номер карты: %s", card_number)
        return None

    try:
        masked_number = card_number[:-4].replace(card_number[:-4], "*" * (len(card_number) - 4)) + card_number[-4:]
        logger.info(f"Успешно замаскирован номер карты: {masked_number}")
        return masked_number
    except Exception as e:
        logger.error("Ошибка при замаскировке номера карты: %s", e)
        return None


def mask_account_number(account_number: str) -> Optional[str]:
    """ Замаскировать номер счета, оставляя только последние 4 цифры видимыми. """

    if not isinstance(account_number, str) or len(account_number) < 4:
        logger.error("Некорректный номер счета: %s", account_number)
        return None

    try:
        masked_account = "*" * (len(account_number) - 4) + account_number[-4:]
        logger.info(f"Успешно замаскирован номер счёта: {masked_account}")
        return masked_account
    except Exception as e:
        logger.error("Ошибка при замаскировке номера счёта: %s", e)
        return None


# Пример использования функций
if __name__ == "__main__":
    print(mask_card_number("1234567812345678"))
    print(mask_account_number("1234567890"))


# def get_mask_card_number(card_number: str) -> str:
# """Функция макскирует номера принимаемых карт"""
# if len(card_number) != 16:
# raise ValueError("Неверная длина номера карты")
# if not card_number.isdigit():
# raise ValueError("Номер должен состоять только из цифр")
# return f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[12:16]}"

# def get_mask_account(account_number: str) -> str:
# """Функция маскирует номер принимаемого счёта"""
# if len(account_number) != 20:
# raise ValueError("Неверная длина номера счёта")
# if not account_number.isdigit():
# raise ValueError("Номер счёта должен состоять только из цифр")
# return f"**{account_number[-4:]}"
