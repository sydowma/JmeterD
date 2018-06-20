from django.conf.urls import url, include
from jmeter import views

urlpatterns = [
    url(r'^files$', views.FilesView.as_view()),
    url(r'^files/(?P<pk>\d+)$', views.FilesDetailView.as_view()),

    url(r'^files/(?P<filename>[^/]+)$', views.FilesUploadView.as_view())
]
