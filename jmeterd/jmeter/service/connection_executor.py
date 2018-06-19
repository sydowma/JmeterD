from fabric import Connection

LOCAL = 'local'
class ConnectionExecutor():

    def __init__(self, connection):
        """
        :param connection Connection for fabric 
        """
        self.connection = connection


    def run(self, command):
        if self.connection.host == LOCAL:
            self.connection.local(command)
        else:
            self.connection.run(command)

    def sudo(self, command):
        if self.connection.host == LOCAL:
            self.connection.local(command)
        else:
            self.connection.sudo(command)
