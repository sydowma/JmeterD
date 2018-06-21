

from __future__ import absolute_import

from celery import Celery, shared_task
from datetime import datetime

app = Celery('tasks', broker='redis://localhost:6379/0',
             backend='redis://localhost:6379/0')
app.conf.update(
    timezone='Asia/Shanghai',
    enable_utc=True
)

@shared_task
def add(x, y):
    return x + y


from .service import jmeter_executor, machine_connection, just_run

@shared_task
def async_run_shell():
    run = just_run.TaskRun()
    run.run_jmeter()

def call_task():
    """
    初始化一个 connection 执行
    """
    async_run_shell.apply_async(args=(), eta=datetime(), task_id='')

    
