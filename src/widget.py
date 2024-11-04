from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(number: str) -> str:
    """Функция маскировки общих данных пользователя карты и номера счёта."""

    if "Счёт" in number:
        return get_mask_account(number)
    else:
        cards = get_mask_card_number(number[-16:])
        new_card = number.replace(number[-16:], cards)
        return new_card


def get_date(old_data: str) -> str:
    """Функция принимает от пользователя на вход строку с датой и возвращает в формате день, месяц и год."""
    data = old_data[0:10].split("-")
    return ".".join(data[::-1])
