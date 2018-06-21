
from django import forms
from django.conf import settings

class FilesForm(forms.Form):
    """
    文件上传表单
    """

    # TODO 验证文件类型后缀
    # if self._upload_valid() is False:
        # return ResponseEntity('error', status.HTTP_400_BAD_REQUEST, errmsg='文件类型后缀错误')



    filename = forms.CharField(
        required=True,
        max_length=50,
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


class TaskForm(forms.Form):
    """
    Task Form
    """
    task_id = forms.IntegerField(
        required=True,
        min_value=1,
        error_messages={
            'required': '请输入任务id',
            'invalid': '错误的任务id',
            'min_value': '错误的任务id'
        }
    )
