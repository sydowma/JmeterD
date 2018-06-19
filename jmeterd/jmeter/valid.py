
"""
表单验证
"""
import rest_framework.status as status_code

from util.http.response_entity import ResponseEntity
from util.form.form_errors import FormErrors

from .form import FilesForm
class Valid(object):

    def __init__(self, form):
        self.form = form

    @property
    def form_errors(self):
        return ResponseEntity(
            self.form.data, status_code.HTTP_400_BAD_REQUEST, FormErrors.errors_message(
                self.form)
        )



class FilesValid(object):

    def __init__(self, data):
        self.form = FilesForm(data)
        self.base_valid = Valid(self.form)
    
    def valid(self):
        if self.form.is_valid():
            pass
        else:
            return self.base_valid.form_errors



