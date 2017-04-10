# -*- coding: utf-8 -*-
import tempfile
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from loader.models import DownloadFile, ResultTask
from loader.forms import UploadFileForm
from loader.tasks import file_length
from loader.api.file import File

def index(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            new_file = DownloadFile(id = form.cleaned_data['id'], file = request.FILES['file'], length=-1)
            new_file.save()
            new_task = ResultTask(id_file=form.cleaned_data['id'], done=False, length=-1, percent=0)
            new_task.save()
            with tempfile.NamedTemporaryFile(delete=False) as f:
                for chunk in request.FILES["file"].chunks():
                    f.write(chunk)
            file_length.delay(new_file.id, f.name)
            return HttpResponseRedirect(reverse('main_page'))
    else:
        form = UploadFileForm()
    # DownloadFile.objects.all().delete()
    # ResultTask.objects.all().delete()
    files = DownloadFile.objects.all()
    return render_to_response(
        'loader/index.html',
        {'files': files, 'form': form, 'max_element': files.last().id if files.last() else 0}
    )
