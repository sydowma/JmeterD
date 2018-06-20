from fabric import Connection
from jmeter.models import Machine
import sys


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
        

class MachineConnection():

    def __init__(self, machine_config):
        """
        :param machine_config 传入一个机器配置类
        :param 
        """
        self.machine_config = MachineConfig(machine_config)
        self.connection = None
        self._connect()


    def _machines(self):
        """
        机器数
        拿出Model中的数据
        """
    
    def _connect(self):
        """
        连接
        """

        """  如果机器数量为空，就使用本地机器  @see connection_executor """
        if self.machine is None:
            self.connection = Connection('local')
        else:
            self.connection = Connection(
                host=self.machine.host,
                user=self.machine.user,
                port=self.machine.port,
                connect_kwargs={
                    'password': self.machine.password
                }
            )

    
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
        
    
    @property
    def status(self):
        """
        机器连接状态
        
        """
