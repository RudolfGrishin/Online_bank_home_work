import pytest
from typing import List, Dict, Any

# Ваши функции
def filter_by_state(data: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """Фильтрует список словарей по значению ключа 'state'"""
    return [item for item in data if item.get("state") == state]

def sort_by_date(data: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """Сортирует список словарей по значению ключа 'date'."""
    return sorted(data, key=lambda x: x["date"], reverse=reverse)

# Фикстура с тестовыми данными
@pytest.fixture
def list_of_dicts() -> List[Dict[str, Any]]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]

# Параметризация для теста filter_by_state
@pytest.mark.parametrize("state, expected_count", [
    ("EXECUTED", 2),
    ("CANCELED", 2),
    ("NON_EXISTENT_STATE", 0)
])
def test_filter_by_state(list_of_dicts: List[Dict[str, Any]], state: str, expected_count: int) -> None:
    filtered_items = filter_by_state(list_of_dicts, state)
    assert len(filtered_items) == expected_count
    assert all(item["state"] == state for item in filtered_items) if expected_count > 0 else True

# Параметризация для теста sort_by_date
@pytest.mark.parametrize("reverse, expected_order", [
    (True, [
        "2019-07-03T18:35:29.512364",  # Самая поздняя
        "2018-10-14T08:21:33.419441",
        "2018-09-12T21:27:25.241689",
        "2018-06-30T02:08:58.425572"   # Самая ранняя
    ]),
    (False, [
        "2018-06-30T02:08:58.425572",  # Самая ранняя
        "2018-09-12T21:27:25.241689",
        "2018-10-14T08:21:33.419441",
        "2019-07-03T18:35:29.512364"   # Самая поздняя
    ])
])
def test_sort_by_date(list_of_dicts: List[Dict[str, Any]], reverse: bool, expected_order: List[str]) -> None:
    sorted_items = sort_by_date(list_of_dicts, reverse)
    assert [item["date"] for item in sorted_items] == expected_order
