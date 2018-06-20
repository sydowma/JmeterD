from django.test import TestCase

from django.conf import settings
import xml.etree.ElementTree as ET
# Create your tests here.
from fabric import Connection
from jmeter.service.check_host import CheckHost
from jmeter.service.jmx_parse import JmxParser, ThreadGroup


EXAMPLE_JMX_PATH = settings.BASE_DIR + '/jmx_file/CSVSample.jmx'

class CheckHostTest(TestCase):

    def setUp(self):
        from fabric import Connection
        self.l = Connection('local')

    def test_cat_host(self):
        c = CheckHost(self.l)
        c.list_host()


class CheckXML(TestCase):

    def setUp(self):
        self.tree = ET.parse(EXAMPLE_JMX_PATH)
        self.root = self.tree.getroot()

    def test_root(self):
        print(self.root.text)
        print(self.root.tag)
        assert self.root.tag == 'jmeterTestPlan'
        assert self.root.attrib['version'] == '1.2'
        assert self.root.attrib['properties'] == '3.2'
        assert self.root.attrib['jmeter'] == '3.3-SNAPSHOT.20170917'

    def test_num_threads(self):
        for elem in self.root.iter(tag="stringProp"):
            if elem.attrib['name'] == 'ThreadGroup.num_threads':
                assert elem.text == '1'
            elif elem.attrib['name'] == 'ThreadGroup.ramp_time':
                assert elem.text == '1'
            elif elem.attrib['name'] == 'ThreadGroup.duration':
                assert elem.text is None

    
    def test_scheduler(self):
        for elem in self.root.iter(tag="boolProp"):
            if elem.attrib['name'] == 'ThreadGroup.scheduler':
                assert elem.text == 'false'

    def test_loops(self):
        for elem in self.root.iter(tag="intProp"):
            if elem.attrib['name'] == 'LoopController.loops':
                assert elem.text == '-1'


    def tearDown(self):
        # self.file.close()
        pass
        

class TestJmxParser(TestCase):

    def setUp(self):
        self.jmx_parser = JmxParser(EXAMPLE_JMX_PATH)
    
    def test_parse_xml(self):

        thread_group = self.jmx_parser.parse_thread_group

        assert thread_group.loops == '-1'
        assert thread_group.num_threads == '1'
        assert thread_group.scheduler == 'false'
        assert len(thread_group.duration) == 0

