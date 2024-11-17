import pytest
from src.widget import mask_account_card, get_date
from src.masks import get_mask_card_number, get_mask_account

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

def get_date(old_data: str) -> str:
    """Функция принимает от пользователя на вход строку с датой и возвращает в формате день, месяц и год."""
    data = old_data[0:10].split("-")
    return ".".join(data[::-1])

# Обновленная фикстура для тестовых данных
@pytest.fixture
def card_numbers():
    return [
        "Alice Johnson 9876543210123456",  # 16 цифр
        "Bob Brown 12345678901234567890"  # 20 цифр
    ]

@pytest.fixture
def dates():
    return [
        ("2023-10-01", "01.10.2023"),
        ("2022-05-15", "15.05.2022")
    ]

# Тесты для функции mask_account_card
@pytest.mark.parametrize("input_number, expected_output", [
    ("Alice Johnson 9876543210123456", "Alice Johnson ************"),
    ("Bob Brown 12345678901234567890", "Bob Brown ********************")
])
def test_mask_account_card(card_numbers, input_number, expected_output):
    assert mask_account_card(input_number) == expected_output

# Тесты для функции get_date
@pytest.mark.parametrize("input_date, expected_output", [
    ("2023-10-01", "01.10.2023"),
    ("2022-05-15", "15.05.2022")
])
def test_get_date(dates, input_date, expected_output):
    assert get_date(input_date) == expected_output
