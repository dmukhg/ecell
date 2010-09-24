from django.forms.util import ErrorList
from ecell2.conman.admin.models import MailList
from django import forms

mailChoices = []
mch = MailList.objects.all()
for item in mch:
    mailChoices.append( (item.pk, item.name) )



class UpdateForm(forms.Form):
    description = forms.CharField( label = "Description" ,max_length = 100 )
    content = forms.CharField( label = "Content", widget = forms.Textarea , max_length = 400 ) 
    url = forms.CharField( label = "Links to" ,max_length = 50, required = True ) 
    active = forms.IntegerField( label = '' ,  widget = forms.HiddenInput( attrs = { 'value' : '0' } ) )
    pk = forms.IntegerField( label = '' , widget = forms.HiddenInput( attrs = { 'value' : '0' } ) )

class MailListForm(forms.Form):
    mList = forms.ChoiceField( widget = forms.CheckboxSelectMultiple, choices=mailChoices)
