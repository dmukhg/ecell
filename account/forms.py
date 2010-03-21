from django.forms.util import ErrorList
from django.contrib.auth.models import User
from django import forms
from choices import *

class SignupForm(forms.Form):
     first_name=forms.CharField(max_length=25,label='First Name')
     last_name=forms.CharField(max_length=25,label='Last Name')
     email=forms.EmailField()
     password1=forms.CharField(max_length=25,widget=forms.PasswordInput,label='Password')
     password2=forms.CharField(max_length=25,widget=forms.PasswordInput,label='Confirm Password')
     sex=forms.ChoiceField(choices=sex_choice)#internally corresponds to character choice of M or F
     occupation=forms.ChoiceField(choices=occupation_choice)#internally corresponds to character choice of M or F
     phno=forms.IntegerField(label='Phone Number')#phone number of the user
     #country=forms.#country of the user
     #state=forms.#state of the user
     institution=forms.CharField(max_length=150,label='Institution')
     address=forms.CharField(max_length=250,widget=forms.Textarea)
     pin=forms.CharField(max_length=10)


     def clean(self):
	     data=self.cleaned_data
	     try:
		     entered_name=data['email']
        	     password1=data['password1']
	             password2=data['password2']
         	     user_qs=User.objects.all()
        	     for user in user_qs:
	        	     if entered_name==user.email:
		        	     self._errors['email']=ErrorList(['Email already registered. Choose a different one.'])
               	     if password1!=password2:
	                 self._errors['password2']=ErrorList(['Passwords do not match'])
                         del data['password1']
	                 del data['password2']
             except:
		     pass
	     return data 

class LoginForm(forms.Form):
     email=forms.EmailField(max_length=25)
     password=forms.CharField(max_length=25,widget=forms.PasswordInput,label='Password')


class TeamCreationForm(forms.Form):
    teamname=forms.CharField(max_length=25)
    competition=forms.ChoiceField()
    member_name=forms.CharField(max_length=25)

class FileUploadForm(forms.Form):
    file=forms.FileField()
