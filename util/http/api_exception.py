
__doc__ = """
rest_framework 异常方法会进入
"""
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        response.data['errcode'] = response.status_code
        response.data['errmsg'] = response.data['detail']

        # 返回请求数据
        response.data['data'] = context.get('kwargs')
        del response.data['detail']  # 删除detail字段

    return response
