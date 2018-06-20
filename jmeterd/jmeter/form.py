
from django import forms
from django.conf import settings

class FilesForm(forms.Form):
    """
    文件上传表单
    """

    filename = forms.CharField(
        required=True,
        max_length=20,
        error_messages={
            'required': '请输入文件名',
            'max_length': '文件名太长了',
            'invalid': '错误的文件名',
            'min_value': '错误的文件名'
        },
    )

    # file = forms.FilePathField(
    #     required=True,
    #     path=settings.BASE_DIR,
    #     error_messages={
    #         'invalid': '错误的文件',
    #     },
    # )
