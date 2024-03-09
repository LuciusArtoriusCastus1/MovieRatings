import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "movieratings.settings")
app = Celery('movieratings')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'send_movie_recommendations': {
        'task': 'movieratings.tasks.send_movie_recommendations',
        'schedule': crontab(minute='0', hour='0', day_of_week='sat', day_of_month='1-7'),  # per month on saturday
    },
    'send_tvshow_recommendations': {
        'task': 'movieratings.tasks.send_tvshow_recommendations',
        'schedule': crontab(minute='0', hour='0', day_of_week='sun', day_of_month='1-7'),  # per month on saturday
    }
}

app.autodiscover_tasks()
