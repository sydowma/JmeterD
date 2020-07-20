from fabric import Connection
from jmeter.models import Machine
import sys

LOCAL = 'local'

__doc__ = """
暂时只支持一个主机器
"""


class LocalMachine():

    @property
    def platform(self):
        """
        检测系统
        """
        return sys.platform

    def is_linux(self):
        return 'linux' in sys.platform or 'Linux' in sys.platform

    def is_mac(self):
        return sys.platform == 'darwin'
    
    def is_windows(self):
        return sys.platform == 'win32'
        

class MachineConfig():

    def __init__(self, machine):
        """
        从 model 转为 实体类
        """
        self.machine = machine

        self.host = None
        self.user = None
        self.port = None
        self.password = None


class Machines():

    def __init__(self):
        self.main_machine = None
        self.subordinate_machines = []
        self._make_machines()

    def _make_machines(self):
        """
        机器数
        拿出Model中的数据
        """
        machines = Machine.objects.all()

        for machine in machines:
            if machine.is_subordinate is False:
                self.main_machine = machine
            else:
                self.subordinate_machines.append(machine)

    def update_status(self):
        """
        连接，并更新 status
        """
        pass


class MachineConnection():

    def __init__(self, machine):
        """
        :param machine_config 传入一个机器配置类
        :param 
        """

        self.machine = machine
        self.connection = None
        self._connect()
    
    def _connect(self):
        """
        连接
        暂时只支持密码
        """

        """  如果机器数量为空，就使用本地机器  @see connection_executor """

        self.connection = Connection(
            host=self.machine.host,
            user=self.machine.user,
            port=self.machine.port,
            connect_kwargs={
                'password': self.machine.password
            }
        )
    
    @property
    def status(self):
        """
        机器连接状态
        
        """

    @property
    def _is_local(self):
        if self.connection.host == LOCAL:
            return True
        else:
            return False

    def run(self, command):
        if self._is_local:
            return self.connection.local(command)
        else:
            return self.connection.run(command)

    def sudo(self, command):
        if self._is_local:
            return self.connection.local(command)
        else:
            return self.connection.sudo(command)
