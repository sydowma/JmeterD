from django.test import TestCase

from django.conf import settings
import xml.etree.ElementTree as ET
# Create your tests here.
from fabric import Connection
from jmeter.service.check_host import CheckHost


class CheckHostTest(TestCase):

    def setUp(self):
        from fabric import Connection
        self.l = Connection('local')

    def test_cat_host(self):
        c = CheckHost(self.l)
        r = c.list_host()


class CheckXML(TestCase):

    def setUp(self):
        self.file = open(settings.BASE_DIR + '/jmx_file/CSVSample.jmx', 'r')
        self.tree = ET.parse(self.file)
        self.root = self.tree.getroot()

    def test_root(self):
        self.root.text
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
                assert len(elem.text) == 0

    
    def test_scheduler(self):
        for elem in self.root.iter(tag="boolProp"):
            if elem.attrib['name'] == 'ThreadGroup.scheduler':
                assert elem.text == 'false'


    def tearDown(self):
        self.file.close()
        
