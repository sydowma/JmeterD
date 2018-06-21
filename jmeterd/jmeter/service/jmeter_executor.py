
from django.conf import settings
from .jmeter_config import JmeterConfig

class JmeterExecutor():
    """
    执行JMeter
    """
    def __init__(self, connection, task):
        """
        :param connection 传入一个connection
        :param 
        """
        self.connection = connection
        self.task = task
        self.jmx = JmeterConfig(self.task.jmx_file.file_path)
        

        self._check_environment()



    def _check_environment(self):
        """
        检查环境是否正常
        """

    def _shell(self, jmeter_path, jmx_file_path, jtl_path, jmeter_report_path):
        """
        """

        return 'sh ' + jmeter_path +'/bin/jmeter.sh -n -t {jmx_file} -l {jtl_path} -e -o {report_path}'.format(
            jmx_file_path, jtl_path, jmeter_report_path
        )
    
    def run_shell(self):
        """
        执行 Shell
        保持 jtl 文件名与报告文件夹名一致
        """
        JMETER_PATH = settings.JMETER_PATH
        JTL_PATH = settings.JTL_PATH
        JMETER_REPORTER_PATH = settings.JMETER_REPORTER_PATH

        thread_group = self.jmx.thread_group

        jmx_file_path = self.task.jmx_file.file_path
        jtl_report_suffix_path = '_' + thread_group.num_threads + '_' + thread_group.duration

        return self.connection.run(self._shell(
            JMETER_PATH, jmx_file_path, JTL_PATH + jtl_report_suffix_path, JMETER_REPORTER_PATH + jtl_report_suffix_path
            ))
        
    

    

    

