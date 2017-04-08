from celery import Celery
import time

app = Celery('tasks')

@app.task(name='loader.tasks.add')
def add(x, y):
    time.sleep(5)
    return x + y