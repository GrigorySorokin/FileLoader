from wsgiref.util import FileWrapper
import os
from loader.models import DownloadFile
from loader.celery import app

@app.task(bind=True, queue='high')
def file_length(self, id, path):
    result = 0
    with open(path, 'rb') as f:
        wrapped_file = FileWrapper(f)
        len_chunks = int(os.path.getsize(path))
        for chunk in wrapped_file:
            result+= len(chunk)
            self.update_state(state='PROGRESS',meta={'percent':int((result/len_chunks)*100), 'result': result})
    file = DownloadFile.objects.get(id=id)
    file.length = result
    file.save()
    return {'percent':100, 'result': result}
