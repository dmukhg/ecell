from django.forms.util import ErrorList
from django.core.files import File
from django.contrib.auth.models import User
from django import forms
from ecell2.upload import choices

class UploadForm(forms.Form):
    get_file=forms.FileField()
    
    def clean(self):
        data = self.cleaned_data
        f = File(data['get_file'])
        print f.name.split('.').pop()


class ImageForm(forms.Form):
    get_image = forms.FileField()
    tag = forms.CharField(max_length = 40, label = "Tag")

    def clean(self):
        data = self.cleaned_data
        type_check = False 
        try:
            f = File( data['get_image'] )
            t = data['tag']
            if t.split(' ').length() is 0:
                self._errors['tag'] = ErrorList(['Tag may not contain spaces'])
        except:
            self._errors['get_image'] = ErrorList(['Please input an image file'])
            return data
        

        type_check = f.name.split('.').pop() not in [ 'jpg' , 'gif' , 'png' ]
        if type_check:
           self._errors['get_image'] = ErrorList(['This is not an image file. Supported types are jpg gif png'])

        return data
