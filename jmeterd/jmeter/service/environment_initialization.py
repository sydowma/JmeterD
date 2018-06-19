from django.conf import settings

JMETER_PATH = settings.JMETER_PATH
class EnvironmentInitialization():
    """
    初始化环境
    """

    def __init__(self, connection):
        """
        :param connection 传入一个已经连接的 connection

        config 配置 JMeter 安装目录
        """
        self.connection = connection


    @property
    def check_java(self):
        """
        返回 True 或者 False
        验证 JAVA_HOME
        """
        result = self.connection.run('java -version')
        if result.ok is False:
            return False

        result_stdout = result.stdout
        if 'version' not in result_stdout:
            return False
        if '1.8' not in result_stdout or '1.9' not in result_stdout:
            return False
        return True


    @property
    def is_jmeter_ready(self):
        """
        返回 True 或者 False
        验证 JMETER_HOME  或者 传入的path
        """
        return self.connection.run('sh ' + JMETER_PATH + '/bin/jmeter.sh' + ' -h').ok

    @property
    def _jmeter_download_url(self):
        return 'http://ftp.cuhk.edu.hk/pub/packages/apache.org//jmeter/binaries/apache-jmeter-4.0.tgz'

    def _curl_jmeter(self):
        return self.connection.run(
            'curl -o apache_jmeter_4.0 ' + self._jmeter_download_url)

    def _tar_jmeter(self):
        self.connection.run('tar zxvf ')

    def _init_java(self):
        pass

    def _init_jmeter(self):
        pass
