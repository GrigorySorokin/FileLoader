from django.conf.urls import url
from loader.views.file import get_file_status

urlpatterns = [
    url(r'get_file_status', get_file_status)
]