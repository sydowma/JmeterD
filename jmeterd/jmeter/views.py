from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from rest_framework import authentication, permissions, status, viewsets
from rest_framework import status, response, parsers, views

from util.http import json_response
from util.http.response_entity import ResponseEntity

from .service import check_host
from .models import (Task, Machine, Files, TaskResult)
from .serializers import (TaskSerializer, MachineSerializer, FilesSerializer, TaskResultSerializer)


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

    def post(self, request, format=None):
        """
        """
        file_obj = request.data['file']
        print(file_obj)



class FilesDetailView(views.APIView):
    """
    文件接口
    """
    # queryset = Files.objects.all()
    # serializer_class = FilesSerializer

    def get(self, request, pk=None):
        """
        """
        queryset = Files.objects.all()
        file = get_object_or_404(queryset, pk=pk)
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
