# API Tests for JSONPlaceholder

Автоматизированные тесты для открытого REST API
[jsonplaceholder.typicode.com](https://jsonplaceholder.typicode.com).

## Что тестируется

- **Posts**: получение списка и отдельного поста, создание (POST), обновление (PUT),
  удаление (DELETE), параметризованные проверки по ID, структура ответа.
- **Users**: получение списка пользователей, структура объекта, формат email,
  посты конкретного пользователя.
- **Негативные сценарии**: запрос несуществующего ресурса, несуществующего эндпоинта,
  пустое тело POST, нестандартный HTTP-метод (PATCH).

## Стек

- Python 3.10+
- Pytest 8.x
- Requests 2.x
- REST, работа с JSON

## Структура

```
api-tests-pytest/
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_posts.py
│   ├── test_users.py
│   └── test_negative.py
├── utils/
│   ├── __init__.py
│   └── api_client.py
├── requirements.txt
├── pytest.ini
├── README.md
└── .gitignore
```

## Как запустить

```bash
# 1. Клонировать репозиторий
git clone https://github.com/<your-username>/api-tests-pytest.git
cd api-tests-pytest

# 2. Создать виртуальное окружение
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux / macOS:
source .venv/bin/activate

# 3. Установить зависимости
pip install -r requirements.txt

# 4. Запустить тесты
pytest
```

Для запуска конкретного файла:

```bash
pytest tests/test_posts.py -v
```

## Что показывает проект

- Навыки написания автотестов на Python с использованием Pytest.
- Работу с HTTP-запросами через Requests и `requests.Session`.
- Понимание REST-архитектуры и кодов ответов (200, 201, 404).
- Парсинг и валидацию JSON-структур.
- Использование фикстур, параметризации и разбиения тестов по модулям.
- Оформление проекта по общепринятой структуре Python-проекта.

## Автор

**<Your Name>** — [GitHub](https://github.com/<cmetanok>)