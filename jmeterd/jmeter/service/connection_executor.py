from fabric import Connection

LOCAL = 'local'
class ConnectionExecutor():

    def __init__(self, connection):
        """
        :param connection Connection for fabric 
        """
        self.connection = connection

    @property
    def _is_local(self):
        if self.connection.host == LOCAL:
            return True
        else:
            return False

    def run(self, command):
        if self._is_local:
            return self.connection.local(command)
        else:
            return self.connection.run(command)

    def sudo(self, command):
        if self._is_local:
            return self.connection.local(command)
        else:
            return self.connection.sudo(command)

    