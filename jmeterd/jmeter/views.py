from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from rest_framework import authentication, permissions, status, viewsets
from rest_framework import status, response, parsers, views

from util.http import json_response
from util.http.response_entity import ResponseEntity

from .service import check_host
from .models import (Task, Machine, Files, TaskResult)
from .serializers import (TaskSerializer, MachineSerializer, FilesSerializer, TaskResultSerializer)

from .valid import Valid

from .form import FilesForm
from .service import file_upload

class MachineViewSet(viewsets.ModelViewSet):
    """
    机器接口
    """
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer

    # def list(self, request):
    #     """
    #     """
    #     pass
    
    # def retrieve(self, request, pk=None):
    #     """
    #     """
    #     pass


class TextCSVParser(parsers.BaseParser):
    media_type = 'text/csv'

    def parse(self, stream, media_type=None, parse_context=None):
        
        return stream.read()

class JmxParse(parsers.BaseParser):
    pass
    

class FilesView(views.APIView):
    """
    文件接口
    """

    

    def get(self, request):
        """
        """
        queryset = Files.objects.all()
        serializer = FilesSerializer(queryset, many=True)
        return json_response.JsonResponse(ResponseEntity(serializer.data))


class FilesUploadView(views.APIView):

    parser_classes = (TextCSVParser,)

    def post(self, request, format=None):
        """
        客户端先检查有没有相同文件
        """
        # files_valid = FilesValid(request)
        # result = files_valid.valid()

        data = {
            'filename': request.META.get('HTTP_FILENAME'),
        }
        form = FilesForm(data)
        if form.is_valid():
            f = file_upload.UploadFile(
                request.data, request.META.get('HTTP_FILENAME'))
            return json_response.JsonResponse(f.upload())
        else:
            return json_response.JsonResponse(Valid.form_errors(form))

        # return json_response.JsonResponse(file_upload.handle_uploaded_file(file_obj, filename))

        # form = FilesForm(filename, request.FILES)
        
        # if form.is_valid():
        #     instance = Files(file_field=request.data)
        #     instance.save()
        #     return json_response.JsonResponse(ResponseEntity(21312))
        # else:
        #     return json_response.JsonResponse(Valid.form_errors(form))


class FilesDetailView(views.APIView):
    """
    文件接口 如果不为空，检测文件状态
    """
    # queryset = Files.objects.all()
    # serializer_class = FilesSerializer

    def get(self, request, name=None):
        """
        """
        queryset = Files.objects.all()
        
        file = get_object_or_404(queryset, name=name)
        """
        到这里说明可以找到file
        """
        file_u = file_upload.FileUtil(name)
        file.status = file_u.is_exists

        serializer = FilesSerializer(file)
        return json_response.JsonResponse(ResponseEntity(serializer.data))

    

class TaskViewSet(viewsets.ViewSet):
    """
    """

    def list(self, request):
        """
        """
        queryset = Task.objects.all()
        serializer = TaskSerializer(queryset, many=True)
        # return response.Response(serializer.data)
        return json_response.JsonResponse(ResponseEntity(serializer.data))
    
    def retrieve(self, request, pk=None):
        """
        """
        queryset = Task.objects.all()
        task = get_object_or_404(queryset, pk=pk)
        serializer = TaskSerializer(task)
        # return response.Response(serializer.data)
        return json_response.JsonResponse(ResponseEntity(serializer.data))

    # def create(self, request):
    #     pass


class TaskResultViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = TaskResult.objects.all()
    serializer_class = TaskResultSerializer
    # def list(self, request):
    #     """
    #     """
    #     pass

    # def retrieve(self, request, pk=None):
    #     """
    #     """
    #     pass


class HostViewSet(viewsets.ViewSet):
    def list(self, request):
        """
        """
        pass

    def retrieve(self, request, pk=None):
        """
        """
        pass


class ConfigViewSet(viewsets.ViewSet):
    def list(self, request):
        """
        """
        pass

    def retrieve(self, request, pk=None):
        """
        """
        pass
