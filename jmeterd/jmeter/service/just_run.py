
from .machine_connection import MachineConnection, Machines
from .jmeter_executor import JmeterExecutor
from .jmeter_config import JmeterConfig
from ..models import Files, Task

from celery import shared_task

class TaskRun():

    def __init__(self, task_id):
        """
        传入 task_id
        """
        self.task_id = task_id
        machines = Machines()
        self.task = self._task
        self.machine_connection = MachineConnection(machines.master_machine)


        self.jmeter_executor = JmeterExecutor(
            self.machine_connection, self.task)


    @shared_task
    def run_jmeter(self):
        """
        
        取出所有数据(目前只支持 local ) TODO 支持远程机器执行   TODO 支持分布式执行
        执行 JMeter
        """

        self.jmeter_executor.run_shell()

    @property
    def _task(self):
        try:
            task = Task.objects.get(pk=self.task_id)
            return task
        except:
            return None
        
