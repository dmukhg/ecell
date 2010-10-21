from django.forms.util import ErrorList
from django.forms import ModelForm
from ecell2.conman.core.models import Incubation, Updates
from django import forms
from mailLists.index import Index

mailChoices = []
for item in Index:
    mailChoices.append( (item['key'], item['description']) )

class updateForm(ModelForm):
    class Meta:
        model = Updates


class MailListForm(forms.Form):
    mList = forms.ChoiceField( widget = forms.CheckboxSelectMultiple, choices=mailChoices)


class incubationForm(ModelForm):
    class Meta:
        model = Incubation
