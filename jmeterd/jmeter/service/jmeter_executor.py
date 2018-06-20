
from django.conf import settings


class JmeterExecutor():
    """
    执行JMeter
    """
    def __init__(self, connection):
        """
        :param connection 传入一个connection
        """
        self.connection = connection

        self._check_environment()

    def _check_environment(self):
        """
        检查环境是否正常
        """

    def _shell(self, jmx_name, jtl_name, report_name):
        JMETER_PATH = settings.JMETER_PATH
        JMX_PATH = settings.JMX_PATH
        JTL_PATH = settings.JTL_PATH
        JMETER_REPORTER_PATH = settings.JMETER_REPORTER_PATH

        return 'sh ' + JMETER_PATH +'/bin/jmeter.sh -n -t {jmx_file} -l {jtl_path} -e -o {report_path}'.format(
            JMETER_PATH, JMX_PATH + jmx_name, JTL_PATH +
            jtl_name, JMETER_REPORTER_PATH + report_name
        )
    
    def _run_shell(self):
        return self.connection.run(self._shell())
        
    

    

    

