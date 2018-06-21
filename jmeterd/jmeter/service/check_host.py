
from __future__ import absolute_import
from .machine_connection import MachineConnection
from python_hosts import Hosts, HostsEntry

IPV4 = 'ipv4'

class CheckHost():
    """
    检查并更改host
    """

    def __init__(self, connection):
        self.connection = MachineConnection(connection)

    @property
    def _get_all_host(self):
        h = ''
        with open(self.host_path, 'r') as f:
            h = f.read()
        return h

    def _is_ipv4(self, string):
        if '.' not in string or ' ' not in string:
            return False
        
        space = string.index(' ')
        string = string[0:space]
        i = 0
        try:
            i = string.split('.')
        except:
            return False
        if len(i) != 4:
            return False
        if isinstance(i, int) is False:
            return False
        return True


    @property
    def _processed_host(self):
        # h = self._get_all_host
        h = self.connection.run(self.cat_host)
        # h_list = h.split('\n')
        # print(dir(h))
        if h.ok is False:
            return []
        h_list = h.stdout.split('\n')
        # h_list = len(h_list)
        # for index, host in enumerate(h_list):

        #     if len(str(host)) <= 2:
        #         h_list.remove(host)
            # else:

                # print(host)
            
            # ip = 1
            # if '#' in host:
            #     sharp_index = host.find('#')
            #     host = host[0:sharp_index].lstrip()
        
        return h_list


    def list_host(self):
        """
        1. 获取所有 host
        2. 根据\n分割
        #3. 遍历所有去掉第一个#之后的信息
        #4. trim
        """

        return self._processed_host
        


    def _clear_host(self):
        """
        """
    


    
    def host_entity(self):
        pass

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
    c.list_host()
