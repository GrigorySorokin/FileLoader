from celery import Celery
from wsgiref.util import FileWrapper
import os
from loader.models import ResultTask, DownloadFile
from celery import shared_task

app = Celery('tasks')

@shared_task()
def file_length(id, path):

    result = 0

    with open(path, 'rb') as f:
        wrapped_file = FileWrapper(f)
        # len_chunks = int(os.path.getsize(path))
        for chunk in wrapped_file:
            result+= len(chunk)
            # instance = ResultTask.objects.get(id_file=id)
            # instance.percent = int((result/len_chunks)*100)
            # instance.save()
    instance = ResultTask.objects.get(id_file=id)
    instance.percent = 100
    instance.done = True
    instance.length = result
    instance.save()
    file = DownloadFile.objects.get(id=id)
    file.length = result
    file.save()
