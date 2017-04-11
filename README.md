# FileLoader

1) Запуск

    Для работы необходимы:

        Django (sudo pip inslall django)
        Celery (sudo pip install celery)
        Djcelery (sudo pip install django-celery)
        RabbitMQ (https://www.rabbitmq.com/download.html)


    После установки запустить в консоле сервисы:

        1) cd путь к проекту
        2) python ./manage.py runserver
        3) python ./manage.py celeryd
        4) python ./manage.py celery beat
        5) python ./manage.py celery worker -l INFO -n worker.high -Q high

    Открыть в браузере 127.0.0.1:8000

2) Что можно улучшить

    Собрать зависимости
    Настроить воркеров/очереди
    Написать тесты