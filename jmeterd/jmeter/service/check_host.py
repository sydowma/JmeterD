
from jmeter.service.connection_executor import ConnectionExecutor

class CheckHost():
    """
    检查并更改host
    """

    def __init__(self, connection):
        self.connection = ConnectionExecutor(connection)

    def check_host(self):
        self.connection.run(self.cat_host)

    @property
    def host_path(self):
        return '/etc/hosts'

    @property
    def cat_host(self):
        return 'cat ' + self.host_path

if __name__ == '__main__':
    from fabric import Connection
    l = Connection('local')
    c = CheckHost(l)
    c.check_host()