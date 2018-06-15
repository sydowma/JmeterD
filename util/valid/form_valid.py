
import sys

import rest_framework.status as status_code

from common.http.api_response_entity import JsonResponseEntity
from common.http.form_errors import FormErrors
from common.http import api_response


class FormValid(object):
    """
    表单验证类
    """

    def __init__(self, form):
        """
        :param form forms.Form
        """
        self.form = form
        """
        取出args
        """
    
    @property
    def form_errors(self):
        return JsonResponseEntity(
            self.form.data, status_code.HTTP_400_BAD_REQUEST, FormErrors.errors_message(
                self.form)
        )
