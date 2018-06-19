


class UploadFile():

    def __init__(self, request):
        self.request = request

    def upload(self, file):
        with open('', 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
