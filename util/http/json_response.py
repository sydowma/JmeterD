# coding: utf-8
from django.utils import six
from rest_framework.response import Response
from rest_framework.serializers import Serializer
import rest_framework.status as status_code

from util.http.response_entity import ResponseEntity

STATUS = 'status'
ERRMSG = 'errmsg'
DATA = 'data'


class JsonResponse(Response):
    """
    从 service 层传过来 ResponseEntity
    在 view 层使用 JsonResponse
    """

    def __init__(self, json_response_entity, content_type=None, template_name=None, exception=None, headers=None):
        # def __init__(self, *agrs):
        """
        Alters the init arguments slightly.
        For example, drop 'template_name', and instead use 'data'.
        Setting 'renderer' and 'media_type' will typically be deferred,
        For example being set automatically by the `APIView`.
        """

        """
        sucesss
        {'key': 'value'}

        error
        { 'errmsg': '111', 'errmsg': 'error1', 'data': {'key': 'value } }
        """

        status = status_code.HTTP_200_OK
        try:

            if json_response_entity.status or json_response_entity.errmsg:
                status = json_response_entity.status
                self.data = json_response_entity.to_dict
            else:

                self.data = json_response_entity.data

        except Exception as e:
            status = status_code.HTTP_500_INTERNAL_SERVER_ERROR
            self.data = {STATUS: status, ERRMSG: "出错，请联系管理员", DATA: {}}

        super(Response, self).__init__(None, status=status)

        """  接口错误时出现 errcode 和 message 否则不出现  """
        # if status >= rest_framework.status.HTTP_400_BAD_REQUEST:

        # if isinstance(data, Serializer):
        #     msg = (
        #         'You passed a Serializer instance as data, but '
        #         'probably meant to pass serialized `.data` or '
        #         '`.error`. representation.'
        #     )
        #     raise AssertionError(msg)

        # template_name = kwargs.get('template_name')
        # headers = kwargs.get('headers')
        # exception = kwargs.get('exception')
        # content_type = kwargs.get('content_type')
        if isinstance(self.data, Serializer):
            msg = (
                'You passed a Serializer instance as data, but '
                'probably meant to pass serialized `.data` or '
                '`.error`. representation.'
            )
            raise AssertionError(msg)

        self.template_name = template_name
        self.exception = exception
        self.content_type = content_type
        # self.content_type = 'application/json'
        if headers:
            for name, value in six.iteritems(headers):
                self[name] = value
