
### Социальная сеть(финальный проект 5 спринт)


### Описание:
- Социальная сеть с возможностью публикации постов, изображений.
- Система подписок на авторов, добавления в избранное.
- Комментарии пользователей.


### Технологии:

- Python 3.10.5
- Django==2.2.28


### Установка:

Клонируем проект:

```bash
git clone https://github.com/themasterid/hw05_final.git
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


### Автор:
Вячеслав Эрлих
