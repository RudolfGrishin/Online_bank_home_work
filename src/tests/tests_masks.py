import pytest
from src.masks import get_mask_card_number, get_mask_account


@pytest.fixture
def valid_card_number() -> str:
    return "1234567812345678"


@pytest.fixture
def valid_account_number() -> str:
    return "12345678901234567890"


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("1234567812345678", "1234 56** **** 5678"),
        ("1234567812345670", "1234 56** **** 5670"),
    ],
)
def test_get_mask_card_number(valid_card_number: str, card_number: str, expected: str) -> None:
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize(
    "card_number",
    [
        "12345678",
        "123456781234567890",
        "1234abcd12345678",
    ],
)
def test_get_mask_card_number_invalid(card_number: str) -> None:
    with pytest.raises(ValueError) as excinfo:
        get_mask_card_number(card_number)
    if len(card_number) < 16:
        assert str(excinfo.value) == "Неверная длина номера карты"
    elif len(card_number) > 16:
        assert str(excinfo.value) == "Неверная длина номера карты"
    else:
        assert str(excinfo.value) == "Номер должен состоять только из цифр"


@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("12345678901234567890", "**7890"),
        ("09876543210987654321", "**4321"),
    ],
)
def test_get_mask_account(valid_account_number: str, account_number: str, expected: str) -> None:
    assert get_mask_account(account_number) == expected


@pytest.mark.parametrize(
    "account_number",
    [
        "1234567890",
        "123456789012345678901234",
        "1234abcd901234567890",
    ],
)
def test_get_mask_account_invalid(account_number: str) -> None:
    with pytest.raises(ValueError) as excinfo:
        get_mask_account(account_number)
    if len(account_number) < 20:
        assert str(excinfo.value) == "Неверная длина номера счёта"
    elif len(account_number) > 20:
        assert str(excinfo.value) == "Неверная длина номера счёта"
    else:
        assert str(excinfo.value) == "Номер счёта должен состоять только из цифр"
