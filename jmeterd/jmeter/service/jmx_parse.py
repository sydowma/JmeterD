
import xml.etree.ElementTree as ET

class ThreadGroup():

    def __init__(self, loops="1", num_threads="1", scheduler="false", duration=""):
        self._loops = loops
        self._num_threads = num_threads
        self._scheduler = scheduler
        self._duration = duration

    @property
    def loops(self):
        return self._loops

    @loops.setter
    def loops(self, value):
        self._loops = value

    @property
    def num_threads(self):
        return self._num_threads
    
    @num_threads.setter
    def num_threads(self, value):
        self._num_threads = value

    @property
    def scheduler(self):
        return self._scheduler

    @scheduler.setter
    def scheduler(self, value):
        self._scheduler = value

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        self._duration = value

    def __repr__(self):
        return 'loops={}\t num_threads={}\t scheduler={}\t duration={}\t'.format(
            self.loops, self.num_threads, self.scheduler, self.duration
        )
    

class JmxParser():
    """
    解析jmx文件
    https://docs.python.org/3.6/library/xml.etree.elementtree.html
    """

    def __init__(self, file_path):
        """
        :param file_path 传入一个 file_path 文件路径
        """
        self.file_path = file_path
        self.thread_group = self.parse_thread_group

    @property
    def parse_thread_group(self):
        
        thread_group = ThreadGroup()

        tree = ET.parse(self.file_path)
        root = tree.getroot()

        for elem in root.iter(tag='intProp'):
            element_name = elem.attrib['name']
            if element_name == 'LoopController.loops':
                thread_group.loops = elem.text

        for elem in root.iter(tag="stringProp"):
            element_name = elem.attrib['name']
            if element_name == 'ThreadGroup.num_threads':
                thread_group.num_threads = elem.text
            elif element_name == 'ThreadGroup.duration':
                thread_group.duration = elem.text or ''

        for elem in root.iter(tag="boolProp"):
            element_name = elem.attrib['name']
            if element_name == 'ThreadGroup.scheduler':
                thread_group.scheduler = elem.text

        return thread_group


    
    
