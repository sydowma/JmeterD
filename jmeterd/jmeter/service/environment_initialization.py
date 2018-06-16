
class EnvironmentInitialization():
    """
    初始化环境
    """

    def __init__(self, connection):
        """
        :param connection 传入一个已经连接的 connection
        """
        self.connection = connection

    @property
    def check_java(self):
        """
        返回 True 或者 False
        验证 JAVA_HOME
        """
        pass
    
    @property
    def check_jmeter(self):
        """
        返回 True 或者 False
        验证 JMETER_HOME  或者 传入的path
        """
        pass

    def _init_java(self):
        pass

    def _init_jmeter(self):
        pass
