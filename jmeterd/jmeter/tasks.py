

from __future__ import absolute_import

from celery import Celery, shared_task

app = Celery('tasks', broker='redis://localhost:6379/0',
             backend='redis://localhost:6379/0')
app.conf.update(
    timezone='Asia/Shanghai',
    enable_utc=True
)

@shared_task
def add(x, y):
    return x + y
