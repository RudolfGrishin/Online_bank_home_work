import pytest
import logging
from io import StringIO
from typing import Generator
from src.decorators import my_function


# Фикстура для настройки логирования
@pytest.fixture(autouse=True)
def setup_logging(capsys: pytest.CaptureFixture) -> Generator[StringIO, None, None]:
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Создаем StringIO для захвата логов
    log_stream = StringIO()
    stream_handler = logging.StreamHandler(log_stream)
    formatter = logging.Formatter("%(message)s")
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    yield log_stream  # Возвращаем поток для захвата логов

    # Удаляем обработчики после теста
    logger.removeHandler(stream_handler)


def test_log_success(setup_logging: StringIO) -> None:
    """Тест успешного выполнения функции с логированием."""
    result = my_function(3, 4)
    assert result == 7

    captured = setup_logging.getvalue()
    assert "Начало выполнения функции: my_function с аргументами: (3, 4), {}" in captured
    assert "my_function ok: 7" in captured


def test_log_failure(setup_logging: StringIO) -> None:
    """Тест обработки исключения в функции с логированием."""
    with pytest.raises(TypeError):
        my_function(3, "4")

    captured = setup_logging.getvalue()
    assert "Начало выполнения функции: my_function с аргументами: (3, '4'), {}" in captured
    assert "my_function error: TypeError. Inputs: (3, '4'), {}" in captured


def test_log_to_file() -> None:
    """Тест записи логов в файл."""
    my_function(5, 6)

    with open("mylog.txt", "r") as f:
        logs = f.read()

    assert "Начало выполнения функции: my_function с аргументами: (5, 6), {}" in logs
    assert "my_function ok: 11" in logs


def test_log_to_file_failure() -> None:
    """Тест записи логов в файл при возникновении исключения."""
    with pytest.raises(TypeError):
        my_function(5, "six")

    with open("mylog.txt", "r") as f:
        logs = f.read()

    assert "Начало выполнения функции: my_function с аргументами: (5, 'six'), {}" in logs
    assert "my_function error: TypeError. Inputs: (5, 'six'), {}" in logs
