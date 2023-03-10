
from .management.commands.runapscheduler import news_sender
from celery import shared_task
import time


@shared_task
def hello():
    time.sleep(10)
    print('Hello, world!')


@shared_task
def sender_news():
    news_sender()