from django import forms

class UploadFileForm(forms.Form):
    id = forms.IntegerField()
    file = forms.FileField()