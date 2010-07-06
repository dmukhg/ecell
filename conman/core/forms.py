from django.forms.util import ErrorList
from django import forms
from models import *

class UpdateForm(forms.Form):
    description = forms.CharField( label = "Description" ,max_length = 100)
    content = forms.CharField( label = "Content", widget = forms.Textarea , max_length = 400 ) 
    url = forms.CharField( label = "Links to" ,max_length = 50, required = True ) 

choice = ['hello','hi','how are']
class SectorForm(forms.Form):
    name = forms.CharField(max_length = 50)
    url = forms.CharField(max_length = 50)
    # parent = forms.ChoiceField( choice )

