

from django.conf import settings
from util.http.response_entity import ResponseEntity
from rest_framework import status

BASE_DIR = settings.BASE_DIR

DATA_DIR = BASE_DIR + '/data_file'
JMX_DIR = BASE_DIR + '/jmx_file'

DIRS = [DATA_DIR, JMX_DIR]

ALLOW_FILE_SUFFIX = ['.csv', '.jmx']

class UploadFile():

    def __init__(self, file, filename):
        self.file = file
        self.filename = filename
        length = len(self.filename)
        self.filename_suffix = self.filename[length - 4: length]
    
    def _upload_valid(self):
        """
        :return True or False
        """
        if self.filename_suffix not in ALLOW_FILE_SUFFIX:
            return False
        else:
            return True
            
    def upload(self):

        if self._upload_valid() is False:
            return ResponseEntity('error', status.HTTP_400_BAD_REQUEST, errmsg='文件类型后缀错误')

        if self.filename_suffix == '.csv':
            DIR = DATA_DIR
        elif self.filename_suffix == '.jmx':
            DIR = JMX_DIR
        
        file_path = DIR + '/' + self.filename

        try:
            f = open(file_path, 'wb+')

            if f.writable() is False:
                return ResponseEntity('error', status.HTTP_400_BAD_REQUEST, errmsg='无法写入')

            f.write(self.file)

            return ResponseEntity('success')
        except Exception as e:
            # print(e)
            return ResponseEntity('error', status.HTTP_400_BAD_REQUEST, errmsg=e)
        finally:
            f.close()



def handle_uploaded_file(file, file_name):
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
