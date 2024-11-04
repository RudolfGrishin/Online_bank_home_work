from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(number: str) -> str:
    """Функция маскировки общих данных пользователя карты и номера счёта."""

    if "Счёт" in number:
        return "Счёт" + get_mask_account(number)
    else:
        cards = get_mask_card_number(number[-16:])
        new_card = number.replace(number[-16:], cards)
        return new_card


print(mask_account_card("Счет 73654108430135874305"))
print(mask_account_card("Visa Platinum 7000792289606361"))
print(mask_account_card("Maestro 7000792289606361"))


def get_date(old_data: str) -> str:
    """Функция принимает от пользователя на вход строку с датой и возвращает в формате день, месяц и год."""
    data = old_data[0:10].split("-")
    return ".".join(data[::-1])


print(get_date("2024-03-11T02:26:18.671407"))
