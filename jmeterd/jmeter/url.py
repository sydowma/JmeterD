from django.conf.urls import url, include
from rest_framework import routers
from .views import MachineViewSet, TaskView, TaskDetailView, TaskViewSet
from jmeter import views


urlpatterns = [
    url(r'^files$', views.FilesView.as_view()),

    # 查询文件
    url(r'^files/(?P<name>[^/]+)$', views.FilesDetailView.as_view()),

    # 上传
    url(r'^upload$', views.FilesUploadView.as_view()),

    # url(r'^task$', views.TaskView.as_view()),
    # url(r'^task/(?P<pk>[\d]+)$', views.TaskDetailView.as_view())
    
    
]


router = routers.DefaultRouter()
router.register(r'machine', MachineViewSet, base_name='machine')
router.register(r'task', TaskViewSet, base_name='task')
urlpatterns += router.urls
