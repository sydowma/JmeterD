from django.conf.urls import url, include
from jmeter import views

urlpatterns = [
    url(r'^files$', views.FilesView.as_view()),

    # 查询文件
    url(r'^files/(?P<name>[^/]+)$', views.FilesDetailView.as_view()),

    # 上传
    url(r'^upload$', views.FilesUploadView.as_view())
]
