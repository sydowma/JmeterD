def ee(c, d):
    return c, d, '你好'


# example
from celery_app import execute

execute.delay('task.all_task.ee', 2, 444)
