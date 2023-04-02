## Django app, реализующее древовидное меню через template tag.

### Для запуска проекта:
#### 1. Установить необходимые пакеты командой: pip install -r requirements.txt.
#### 2. Провести миграции командой: python manage.py migrate.
#### 3. Создать суперпользователя для редактирования данных командой: python manage.py createsuperuser.
#### 4. Пример данных находится в файле fixtures. 
#### Подгрузить можно командой: python manage.py load_data fixtures/menu.json.
#### 5. В файле index.html раскомментировать код "рисования меню".
#### 6. Запустить проект командой: python manage.py runserver.