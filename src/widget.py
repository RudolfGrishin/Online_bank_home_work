from masks import get_mask_account, get_mask_card_number


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


def get_date(user_date: str) -> str:
    """Функция принимает от пользователя на вход строку с датой и возвращает в формате день, месяц и год."""
    slice_date = user_date[:10]
    date_clear = ""
    for one_symbol in range(len(slice_date)):
        if slice_date[one_symbol].isdigit():
            date_clear += slice_date[one_symbol]
        else:
            date_clear += ""
    date_clear_split = date_clear.split()
    split_date = date_clear_split[::-1]
    result = ".".join(split_date)
    return result
