from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from rest_framework import authentication, permissions, status, viewsets
from rest_framework import status, response

from util.http import json_response
from util.http.response_entity import ResponseEntity

from .service import check_host
from .models import (Task, Machine)
from .serializers import (TaskSerializer, MachineSerializer)


class MachineViewSet(viewsets.ViewSet):
    """
    机器接口
    """

    def list(self, request):
        """
        """
        pass
    
    def retrieve(self, request, pk=None):
        """
        """
        pass




class FilesViewSet(viewsets.ViewSet):
    """
    文件接口
    """

    def list(self, request):
        """
        """
        pass

    def retrieve(self, request, pk=None):
        """
        """
        pass


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


class TaskResult(viewsets.ViewSet):
    def list(self, request):
        """
        """
        pass

    def retrieve(self, request, pk=None):
        """
        """
        pass


class Host(viewsets.ViewSet):
    def list(self, request):
        """
        """
        pass

    def retrieve(self, request, pk=None):
        """
        """
        pass


class Config(viewsets.ViewSet):
    def list(self, request):
        """
        """
        pass

    def retrieve(self, request, pk=None):
        """
        """
        pass
