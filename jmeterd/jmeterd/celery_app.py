__doc__ = """
https://segmentfault.com/a/1190000010112848
"""

from importlib import import_module, reload

from celery import Celery

app = Celery('tasks', broker='redis://localhost:6379/0',
             backend='redis://localhost:6379/0')
app.conf.update(
    timezone='Asia/Shanghai',
    enable_utc=True
)

app.conf.CELERY_IMPORTS = ['task', 'task.all_task']


def import_string(import_name):
    import_name = str(import_name).replace(':', '.')
    modules = import_name.split('.')
    mod = import_module(modules[0])
    for comp in modules[1:]:
        if not hasattr(mod, comp):
            reload(mod)
        mod = getattr(mod, comp)
    return mod


@app.task
def execute(func, *args, **kwargs):
    func = import_string(func)
    return func(*args, **kwargs)

import datetime

@app.task
def interval(func, seconds, args=(), task_id=None):
    next_run_time = datetime.datetime.now() + datetime.timedelta(seconds=seconds)
    kwargs = dict(args=(func, seconds, args), eta=next_run_time)
    if task_id is not None:
        kwargs.update(task_id=task_id)
    interval.apply_async(**kwargs)
    func = import_string(func)
    return func(*args)

from inspect import getmembers, isfunction

def get_tasks(module='task'):
    return [{
        'name': 'task:{}'.format(f[1].__name__),
        'doc': f[1].__doc__,
    } for f in getmembers(import_module(module), isfunction)]
