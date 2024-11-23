import pytest
from typing import Iterator, List, Tuple


# Функция для генерации номеров банковских карт
def card_number_generator(start: int, end: int) -> Iterator[str]:
    """Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX."""
    for number in range(start, end + 1):
        formatted_number = f"{number:016d}"
        yield f"{formatted_number[:4]} {formatted_number[4:8]} {formatted_number[8:12]} {formatted_number[12:16]}"


# Фикстура для тестовых данных
@pytest.fixture(
    params=[
        (
            1,
            10,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005",
                "0000 0000 0000 0006",
                "0000 0000 0000 0007",
                "0000 0000 0000 0008",
                "0000 0000 0000 0009",
                "0000 0000 0000 0010",
            ],
        ),
        (0, 0, ["0000 0000 0000 0000"]),
        (
            9999999999999999,
            10000000000000000,
            [
                "9999 9999 9999 9999",
                "1000 0000 0000 0000",
            ],
        ),
        (5, 4, []),  # Ожидаем пустой список
    ]
)
def card_number_test_data(request: pytest.FixtureRequest) -> Tuple[int, int, List[str]]:
    """Фикстура для тестовых данных, возвращает параметры для теста."""
    return request.param  # Здесь мы возвращаем параметр, который уже соответствует типу


# Параметризованный тест
def test_card_number_generator(card_number_test_data: Tuple[int, int, List[str]]) -> None:
    start_value, end_value, expected_numbers = card_number_test_data
    result = list(card_number_generator(start_value, end_value))
    assert result == expected_numbers
