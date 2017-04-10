from celery import Celery

app = Celery('loader',
             broker='amqp://guest@localhost//',
             backend='amqp://guest@localhost//',
             include=['loader.tasks']
             )

app.conf.update(
    CELERY_TASK_SERIALIZER='json',
    CELERY_RESULT_SERIALIZER='json',
    CELERY_ACCEPT_CONTENT=['json'],
    CELERY_TIMEZONE='Europe/Moscow',
    CELERY_ENABLE_UTC=True
)
