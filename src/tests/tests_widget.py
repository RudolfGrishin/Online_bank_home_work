import pytest
from src.widget import mask_account_card, get_date

@pytest.fixture
def test_data():
    return [
        ("Пользователь 1234567812345678", "Пользователь 1234 56** **** 5678"),  # Тест для карты
        ("Пользователь 12345678901234567890", "Пользователь **7890"),  # Тест для счета
        ("Пользователь 12345678", "Пользователь 12345678"),  # Неверный номер
    ]

@pytest.mark.parametrize("input_data, expected_output", [
    ("Пользователь 1234567812345678", "Пользователь 1234 56** **** 5678"),  # Тест для карты
    ("Пользователь 12345678901234567890", "Пользователь **7890"),  # Тест для счета
])
def test_mask_account_card(input_data, expected_output):
    assert mask_account_card(input_data) == expected_output

def test_mask_account_card_invalid():
    with pytest.raises(ValueError):
        mask_account_card("Пользователь 12345678")  # Неверный номер

@pytest.mark.parametrize("input_date, expected_output", [
    ("2023-10-05", "05.10.2023"),  # Корректная дата
    ("2020-01-01", "01.01.2020"),  # Корректная дата
])
def test_get_date(input_date, expected_output):
    assert get_date(input_date) == expected_output

