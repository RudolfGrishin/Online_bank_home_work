import pytest
from src.widget import mask_account_card, get_date


@pytest.fixture
def test_data() -> list[tuple[str, str]]:
    return [
        ("Пользователь 1234567812345678", "Пользователь 1234 56** **** 5678"),
        ("Пользователь 12345678901234567890", "Пользователь **7890"),
        ("Пользователь 12345678", "Пользователь 12345678"),
    ]


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        ("Пользователь 1234567812345678", "Пользователь 1234 56** **** 5678"),
        ("Пользователь 12345678901234567890", "Пользователь **7890"),
    ],
)
def test_mask_account_card(input_data: str, expected_output: str) -> None:
    assert mask_account_card(input_data) == expected_output


def test_mask_account_card_invalid() -> None:
    with pytest.raises(ValueError):
        mask_account_card("Пользователь 12345678")


@pytest.mark.parametrize(
    "input_date, expected_output",
    [
        ("2023-10-05", "05.10.2023"),
        ("2020-01-01", "01.01.2020"),
    ],
)
def test_get_date(input_date: str, expected_output: str) -> None:
    assert get_date(input_date) == expected_output
