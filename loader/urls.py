from django.conf.urls import url
from loader.views.file import file, get_file_status

urlpatterns = [
    url(r'file/$', file, name='file_loader'),
    url(r'get_file_status', get_file_status)
]