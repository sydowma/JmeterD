from fabric import Connection
from jmeter.models import Machine
import sys

class LocalMachine():
    
    @property
    def platform(self):
        """
        检测系统
        """
        return sys.platform

    def is_linux(self):
        return sys.platform == 'linux2'
    
    def is_mac(self):
        return sys.platform == 'darwin'
    
    def is_windows(self):
        return sys.platform == 'win32'
        


class MachineConnection():

    def __init__(self, machine):
        """
        """
        self.machine = machine
        self._connect()
    
    def _connect(self):
        """
        连接
        """

        """  如果机器数量为空，就使用本地机器  """
        if self.machine is None:
            pass
    
    @property
    def status(self):
        """
        机器连接状态
        
        """
