class Host():

    def __init__(self, ip, server):
        self._ip = ip
        self._server = server
    
    @property
    def ip(self):
        return self._ip

    @ip.setter
    def ip(self, value):
        self._ip = value

    @property
    def server(self):
        return self._server

    @server.setter
    def server(self, value):
        self._server = value

    
    def __repr__(self):
        return '{} {}'.format(self.ip, self.server)

    