
class ResponseEntity(object):
    """
    返回JSON Response
    """

    def __init__(self, data, status=None, errmsg=None):
        self._data = data
        self._status = status
        self._errmsg = errmsg

    def __len__(self):
        return len(self.data)

    @property
    def data(self):
        """
        get data
        """
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    @property
    def errmsg(self):
        return self._errmsg

    @errmsg.setter
    def errmsg(self, value):
        self._errmsg = value

    @property
    def to_dict(self):
        """
        object to dict
        """
        return {
            'data': self._data,
            'status': self._status,
            'errmsg': self._errmsg
        }
