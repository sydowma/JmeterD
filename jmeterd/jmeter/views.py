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

from .form import FilesForm, TaskForm
from .service import file_upload
from .parser import TextCSVParser, JmxParser
from .tasks import async_run_task

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


class TaskRunView(views.APIView):
    """
    任务执行
    """

    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            async_run_task(form.cleaned_data['task_id'])
            return json_response.JsonResponse('success')
        else:
            return json_response.JsonResponse(Valid.form_errors(form))



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

    parser_classes = (TextCSVParser, JmxParser)

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

        """
        当文件状态属性更新时同时更新数据库
        """
        if file_u.is_exists is not file.status:
            file.status = file_u.is_exists
            file.save()
        

        serializer = FilesSerializer(file)
        return json_response.JsonResponse(ResponseEntity(serializer.data))

    
class TaskView(views.APIView):
    """
    """
    # queryset = Task.objects.all()
    # serializer_class = TaskSerializer

    def get(self, request):
        """
        """
        queryset = Task.objects.all()
        serializer = TaskSerializer(queryset, many=True)
        # return response.Response(serializer.data)
        return json_response.JsonResponse(ResponseEntity(serializer.data))


class TaskViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDetailView(views.APIView):

    def get(self, request, pk=None):
        """
        """
        queryset = Task.objects.all()
        task = get_object_or_404(queryset, pk=pk)
        serializer = TaskSerializer(task)
        # return response.Response(serializer.data)
        return json_response.JsonResponse(ResponseEntity(serializer.data))

    def put(self, request, pk):
        """
        """
        queryset = Task.objects.all()
        task = get_object_or_404(queryset, pk=pk)
        
        serializer = TaskSerializer(task)
        return json_response.JsonResponse(ResponseEntity(serializer.data))




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
