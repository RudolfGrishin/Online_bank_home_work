import logging
from functools import wraps
from typing import Callable, Optional, Any


def log(filename: Optional[str] = None) -> Callable:
    """
    Декоратор для логирования начала и конца выполнения функции, а также ее результатов или ошибок.

    :param filename: Имя файла для записи логов. Если не указано, логи выводятся в консоль.
    """

    # Настройка логирования
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Установка обработчика
    if filename:
        handler = logging.FileHandler(filename)
    else:
        handler = logging.StreamHandler()

    logger.addHandler(handler)

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                logger.info(f"Начало выполнения функции: {func.__name__} с аргументами: {args}, {kwargs}")
                result = func(*args, **kwargs)
                logger.info(f"{func.__name__} ok: {result}")
                return result
            except Exception as e:
                logger.error(f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}")
                raise

        return wrapper

    return decorator


@log(filename="mylog.txt")
def my_function(x: int, y: int) -> int:
    return x + y


# Пример вызова функции
my_function(1, 2)
