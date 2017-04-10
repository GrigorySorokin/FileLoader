from django.http import HttpResponse
from loader.api.storage import Storage
from loader.tasks import file_length
from loader.models import DownloadFile
import json

def get_file_status(request):
    if request.method == 'POST':
        file_id = request.POST.get('file_id')
        try:
            id_task = Storage().get_task(file_id)
        except:
            file = DownloadFile.objects.get(id=file_id)
            result = {
                'percent': 100,
                'done': True,
                'length': file.length if file else 'ERROR'
            }
            return HttpResponse(json.dumps(result), content_type="application/json")
        task = file_length.AsyncResult(id_task)

        print(task.status)
        print(task.info)
        print(task.ready())

        if task.ready():
            result = {
                'percent': 100,
                'done': True,
                'length': task.result
            }
            return HttpResponse(json.dumps(result), content_type="application/json")
        print(task.status)
        print(task.info)
        info = task.info
        result = {
            'percent': info['percent'] if info else 0,
            'done': False,
            'length': info['result']if info else 0
        }
        return HttpResponse(json.dumps(result), content_type="application/json")


