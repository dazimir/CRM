# CRM
Проект CRM пишу в Pycharm


pip install django


pip install psycopg2-binary  (для Ubuntu)  или без -binary для windows

в pgAdmin4 создаем базу и пользователя с правами суперюзер


вносим настройки в ![image](https://user-images.githubusercontent.com/72926812/207679691-ec444fc5-35a9-4627-a25f-c34e7f5edc4e.png)

удаляем папку migrations ![image](https://user-images.githubusercontent.com/72926812/207680106-40841b54-4ed0-464e-aefb-2f18a2447fa8.png)

выполняем миграции 'python manage.py makemigrations'   и  'python manage.py migrate'

создаем суперюзера 'python manage.py createsuperuser'  имя и пароль которое задавали при создании БД

запускаем 'python manage.py runserver'
