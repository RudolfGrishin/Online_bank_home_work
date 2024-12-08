import os
import logging

# Создание директории logs, если она не существует
log_dir = "../logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Путь к файлу логов
log_file_path = os.path.join(log_dir, "masks.log")
print(f"Логи будут записываться в: {os.path.abspath(log_file_path)}")

# Создание отдельного логгера
logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)  # Установлен уровень логирования не меньше, чем DEBUG

# Настройка обработчика для логера
file_handler = logging.FileHandler(log_file_path, mode="w", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)

# Настройка форматировщика для логера
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)

# Добавление обработчика к логгеру
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """ Маскирует номер карты, оставляя только последние 4 цифры видимыми. """
    try:
        if len(card_number) != 16:
            logger.error("Неверная длина номера карты")  # Логирование ошибки
            raise ValueError("Неверная длина номера карты")
        if not card_number.isdigit():
            logger.error("Номер должен состоять только из цифр")  # Логирование ошибки
            raise ValueError("Номер должен состоять только из цифр")

        masked_number = f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[12:16]}"
        logger.info(f"Успешно замаскирован номер карты: {masked_number}")  # Логирование успешного случая
        return masked_number
    except ValueError as e:
        logger.error(f"Ошибка при маскировке номера карты: {e}")  # Логирование ошибки
        raise


def get_mask_account(account_number: str) -> str:
    """ Маскирует номер счета, оставляя только последние 4 цифры видимыми. """
    try:
        if len(account_number) != 20:
            logger.error("Неверная длина номера счёта")  # Логирование ошибки
            raise ValueError("Неверная длина номера счёта")
        if not account_number.isdigit():
            logger.error("Номер счёта должен состоять только из цифр")  # Логирование ошибки
            raise ValueError("Номер счёта должен состоять только из цифр")

        masked_account = f"**{account_number[-4:]}"
        logger.info(f"Успешно замаскирован номер счёта: {masked_account}")  # Логирование успешного случая
        return masked_account
    except ValueError as e:
        logger.error(f"Ошибка при маскировке номера счёта: {e}")  # Логирование ошибки
        raise


if __name__ == "__main__":
    try:
        # Примеры с корректными данными
        print(get_mask_card_number("1234567812345678"))
        print(get_mask_account("12345678901234567890"))

        # Примеры с некорректными данными для тестирования логирования ошибок
        print(get_mask_card_number("12345"))
        print(get_mask_account("123"))
        print(get_mask_account("12345678901234567890abc"))
    except Exception as e:
        logger.error(f"Произошла ошибка: {e}")


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
