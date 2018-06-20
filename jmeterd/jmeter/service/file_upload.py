

from django.conf import settings

BASE_DIR = settings.BASE_DIR

DATA_DIR = BASE_DIR + '/data_file'
class UploadFile():

    def __init__(self, request):
        self.request = request


def handle_uploaded_file(file, file_name):
    file_path = DATA_DIR + '/' + file_name

    try:
        f = open(file_path, 'wb+')
        f.write(file)
        return True
    except Exception as e:
        print(e)
        return False
    finally:
        f.close()
    # with open(file_path, 'wb+') as destination:
    #     # for chunk in file.chunks():
    #         # destination.write(chunk)
    #     destination.write(file)
