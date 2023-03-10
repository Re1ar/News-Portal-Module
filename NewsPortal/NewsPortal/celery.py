# Импортируем библиотеку для взаимодействия с операционной системой
import os
# Импортируем библиотеку "Celery"
from celery import Celery
from celery.schedules import crontab

# Связываем настройки Django с настройками Celery через переменную окружения
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewsPortal.settings')

# Создаем экземпляр приложения Celery и устанавливаем для него файл конфигурации.
# Мы также указываем пространство имен, чтобы Celery сам находил все необходимые настройки в файле settings.py
# Он их будет искать по шаблону: "CELERY_***"
app = Celery('NewsPortal')
app.config_from_object('django.conf:settings', namespace='CELERY')

# Указываем Celery автоматически искать задания в файлах "tasks.py" каждого приложения проекта
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'action_every_monday_8am': {
        'task': 'news.tasks.sender_news',
        'schedule': crontab(hour=8, minute=0, day_of_week='monday'),
    },
}

