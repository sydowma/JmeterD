
import sys

import rest_framework.status as status_code

from util.http.response_entity import ResponseEntity
from util.form.form_errors import FormErrors


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
        return ResponseEntity(
            self.form.data, status_code.HTTP_400_BAD_REQUEST, FormErrors.errors_message(
                self.form)
        )
