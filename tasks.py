from celery import Celery

from src.funcs import add

app = Celery(
    'tasks', 
    broker='redis://redis:6379/0', 
    backend='redis://redis:6379/0'
)

@app.task
def task_add(x, y):
    return add(x, y)