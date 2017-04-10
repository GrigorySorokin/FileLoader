# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from loader.models import DownloadFile, ResultTask
from loader.forms import UploadFileForm
import json

def file(request):
    # Handle file upload
    if request.method == 'POST':
        print('POST')
        form = UploadFileForm(request.POST, request.FILES)
        print(form)
        print(request)
        if form.is_valid():
            print('Valid')
            newdoc = DownloadFile(file = request.FILES['file'], length=-1)
            newdoc.save()
            documents = DownloadFile.objects.all()
            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('file_loader'))
    else:
        form = UploadFileForm() # A empty, unbound form

    # Load documents for the list page

    documents = DownloadFile.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'loader/list.html',
        {'documents': documents, 'form': form}
    )


    # file_full_path = "/tmp/{0}".format(offset)
    # response = StreamingHttpResponse((line for line in open(file_full_path, 'r')))
    # response['Content-Disposition'] = "attachment; filename={0}".format(offset)
    # response['Content-Length'] = os.path.getsize(file_full_path)
    # return response

def get_file_status(request):
    if request.method == 'POST':
        file_id = request.POST.get('file_id')
        print(1)
        res = ResultTask.objects.get(id_file=file_id)
        print(2)
        result = {
            'percent': res.percent,
            'done': res.done,
            'length': res.length
        }
        res.save()
        return HttpResponse(json.dumps(result), content_type="application/json")
        # return HttpResponse(json.dumps({}), content_type="application/json")