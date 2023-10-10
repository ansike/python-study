# myapp/tasks.py

from celery import shared_task
from time import sleep

@shared_task
def add(x, y):
    print('starting')
    sleep(3)
    print('done')
    return x + y
