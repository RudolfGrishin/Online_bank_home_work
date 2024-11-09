# Название проекта
FC_BARCELONA.
## Описание
Этот проект содержит функции для фильтрации и сортировки списка словарей, содержащих информацию о транзакциях. Каждая транзакция представлена в виде словаря с полями `id`, `state` и `date`.
## Установка
1. Склонируйте репозиторий:
2. git@github.com:RudolfGrishin/Online_bank_home_work.git
3. Установите зависимости:
```
[tool.poetry]
name = "online-bank-projects"
version = "0.1.0"
description = ""
authors = ["Your Name <you@example.com>"]
readme = "README.md"

[tool.poetry.dependencies]
python = "^3.13"


[tool.poetry.group.lint.dependencies]
flake8 = "^7.1.1"
mypy = "^1.13.0"
black = "^24.10.0"
isort = "^5.13.2"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

[tool.black]
line-length = 119
exclude = '.git'

[tool.mypy]
disallow_untyped_defs = true
no_implicit_optional = true
warn_return_any = true
exclude = 'venv'

[tool.isort]
line_length = 119
```
## Использование:

1. Необходимо использовать готовые функции для маскировки в приложении банка, различных карт, счётов или сортировку а так же фильтрацию нужным данным для банковской системы.

## Документация:

[GitHub]  https://github.com/RudolfGrishin/Online_bank_home_work/tree/feature/homework_10_1

## Лицензия:

Проект распространяется под [лицензией MIT](LICENSE)
