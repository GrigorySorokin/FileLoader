from django.conf.urls import url
from loader.views.file import file

urlpatterns = [
    url(r'file/(\d*)/$', file, name='file_loader')
]