

from .jmx_parse import ThreadGroup, JmxParser

class JmeterConfig():
    """
    JMeter 配置相关
    """

    def __init__(self, jmx_path):
        jmx_parser = JmxParser(jmx_path)
        self.thread_group = jmx_parser.thread_group
    
