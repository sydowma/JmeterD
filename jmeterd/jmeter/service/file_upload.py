import os

from django.conf import settings
from util.http.response_entity import ResponseEntity
from rest_framework import status

from ..models import Files

BASE_DIR = settings.BASE_DIR

DATA_DIR = BASE_DIR + '/data_file'
JMX_DIR = BASE_DIR + '/jmx_file'

DIRS = [DATA_DIR, JMX_DIR]

ALLOW_FILE_SUFFIX = ['.csv', '.jmx']


class FileUtil():

    def __init__(self, filename):

        self.filename = filename
        

        length = len(self.filename)
        self.filename_suffix = self.filename[length - 4: length]

        if self.filename_suffix == '.csv':
            DIR = DATA_DIR
        elif self.filename_suffix == '.jmx':
            DIR = JMX_DIR

        self.file_path = DIR + '/' + self.filename

    @property
    def is_exists(self):
        """
        判断是否存在
        https://stackoverflow.com/questions/82831/how-do-i-check-whether-a-file-exists
        :return Bool
        """
        try:
            st = os.stat(self.file_path)
        except os.error:
            return False
        return True


class UploadFile(FileUtil):

    def __init__(self, file, filename):
        
        super().__init__(filename)
        self.file = file

    
    def _upload_valid(self):
        """
        :return True or False
        """
        if self.filename_suffix not in ALLOW_FILE_SUFFIX:
            return False
        else:
            return True

    def _save_file(self, file_path):
        """
        1. 先检查如果有相同名称的更改
        """
        file_exist = Files.objects.filter(name=self.filename)
        if file_exist:
            file = file_exist[0]
        else:
            file = Files()
        file.file_path = file_path
        file.name = self.filename
        file.save()

            
    def upload(self):

        file_path = self.file_path
        try:
            f = open(file_path, 'wb+')

            if f.writable() is False:
                return ResponseEntity('error', status.HTTP_400_BAD_REQUEST, errmsg='无法写入')

            f.write(self.file)

            self._save_file(file_path)

            return ResponseEntity('success')
        except Exception as e:
            # print(e)
            return ResponseEntity('error', status.HTTP_400_BAD_REQUEST, errmsg=e.args)
        finally:
            f.close()


        

def handle_uploaded_file(file, file_name):
    """
    弃用
    """
    length = len(file_name)
    if file_name[length - 4: length] == '.csv':
        DIR = DATA_DIR
    elif file_name[length - 4: length] == '.jmx':
        DIR = JMX_DIR
    else:
        return ResponseEntity('error', status.HTTP_400_BAD_REQUEST, errmsg='文件类型后缀错误')

    file_path = DIR + '/' + file_name

    try:
        f = open(file_path, 'wb+')

        if f.writable() is False:
            return ResponseEntity('error', status.HTTP_400_BAD_REQUEST, errmsg='无法写入')

        f.write(file)
        
        return ResponseEntity('success')
    except Exception as e:
        # print(e)
        return ResponseEntity('error', status.HTTP_400_BAD_REQUEST, errmsg=e)
    finally:
        f.close()
    # with open(file_path, 'wb+') as destination:
    #     # for chunk in file.chunks():
    #         # destination.write(chunk)
    #     destination.write(file)
