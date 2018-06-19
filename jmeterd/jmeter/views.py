from django.shortcuts import render

# Create your views here.
from rest_framework import authentication, permissions, status, viewsets
from rest_framework import status
from util.http import json_response, response_entity

from .service import check_host


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
        pass
    
    def retrieve(self, request, pk=None):
        """
        """
        pass


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
