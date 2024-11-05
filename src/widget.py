from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(number: str) -> str:
    """Функция маскировки общих данных пользователя карты и номера счёта."""
    original_number = number.split()[-1]
    if len(original_number) == 16:
        mask_number_1 = get_mask_card_number(original_number)
        result = f"{number[:-16]}{mask_number_1}"
    elif len(original_number) == 20:
        mask_number_2 = get_mask_account(original_number)
        result = f"{number[:-20]}{mask_number_2}"
    return result


def get_date(old_data: str) -> str:
    """Функция принимает от пользователя на вход строку с датой и возвращает в формате день, месяц и год."""
    data = old_data[0:10].split("-")
    return ".".join(data[::-1])
