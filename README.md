ФИНАЛЬНЫЙ ПРОЭКТ 5 спринта.

Социальная сеть с возможностью публикации постов, изображений, системой подписок на авторов, добавления в избранное, комментариев пользователей.

Стек:

- Python 3.10.5
- Django==2.2.28

### Настройка и запуск на ПК

Клонируем проект:

```bash
git clone https://github.com/themasterid/hw05_final.git
```

или

```bash
git clone git@github.com:themasterid/hw05_final.git
```

Устанавливаем виртуальное окружение:

```bash
python -m venv venv
```

Активируем виртуальное окружение:

```bash
source venv/Scripts/activate
```

Устанавливаем зависимости:

```bash
python -m pip install --upgrade pip
```
```bash
pip install -r requirements.txt
```

Применяем миграции:

```bash
python yatube/manage.py makemigrations
python yatube/manage.py migrate
```

Создаем супер пользователя:

```bash
python yatube/manage.py createsuperuser
```

Запускаем проект:

```bash
python yatube/manage.py runserver localhost:80
```

Проект будет доступен по адресу http://localhost/
Заходим в http://localhost/admin и создаем группы и записи.

[![CI](https://github.com/yandex-praktikum/hw05_final/actions/workflows/python-app.yml/badge.svg?branch=master)](https://github.com/yandex-praktikum/hw05_final/actions/workflows/python-app.yml)
