import json

from django.http import HttpResponse

from loader.api.storage import Storage
from loader.tasks import file_length
from loader.models import DownloadFile


def get_file_status(request):
    if request.method == 'POST':
        file_id = request.POST.get('file_id')

        try:
            id_task = Storage().get_task(file_id)
        except:
            file = DownloadFile.objects.get(id=file_id)
            return HttpResponse(json.dumps({
                'percent': 100,
                'done': True,
                'length': file.length if file else 'ERROR'
            }), content_type="application/json")

        task = file_length.AsyncResult(id_task)
        if task.ready():
            return HttpResponse(json.dumps({
                'percent': 100,
                'done': True,
                'length': task.result['result']
            }), content_type="application/json")

        info = task.info
        return HttpResponse(json.dumps({
            'percent': info['percent'] if info else 0,
            'done': False,
            'length': info['result']if info else 0
        }), content_type="application/json")
