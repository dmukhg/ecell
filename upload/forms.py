from django.forms.util import ErrorList
from django.core.files import File
from django.contrib.auth.models import User
from django import forms
import choices

class UploadForm(forms.Form):
    get_file=forms.FileField()
    
    def clean(self):
        data = self.cleaned_data
        f = File(data['get_file'])
        print f.name.split('.').pop()


class ImageForm(forms.Form):
    get_image = forms.FileField()

    def clean(self):
        data = self.cleaned_data
        f = File( data['get_image'] )
        print f.name.split('.').pop()
