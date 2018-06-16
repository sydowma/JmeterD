
class EnvironmentInitialization():
    """
    初始化环境
    """

    def __init__(self, connection):
        """
        :param connection 传入一个已经连接的 connection
        """
        self.connection = connection

    def _init_java(self):
        pass

    def _init_jmeter(self):
        pass
