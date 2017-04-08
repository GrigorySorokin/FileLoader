# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from loader.models import DownloadFile
from loader.forms import UploadFileForm

def file(request, offset):
    # Handle file upload
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = DownloadFile(file = request.FILES['file'])
            newdoc.save()
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
