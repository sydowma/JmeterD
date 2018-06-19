from django.test import TestCase

# Create your tests here.
from fabric import Connection
from jmeter.service.check_host import CheckHost


class CheckHostTest(TestCase):

    def setUp(self):
        from fabric import Connection
        self.l = Connection('local')

    def test_cat_host(self):
        c = CheckHost(self.l)
        r = c.check_host()
        
