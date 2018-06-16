

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
    
    def _run_shell(self):
        return 'sh {path}jmeter.sh -n -t {jmx_file} -l {jtl_path} -e -o {report_path}'.format()

    

    

