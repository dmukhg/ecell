from django import forms

class PreRegForm(forms.Form):
    name = forms.CharField(max_length=30, label="Name")
    rollno = forms.CharField(max_length=10, label="Roll No.")
    email = forms.EmailField(max_length=30, label="Email Address")
    phno = forms.CharField(max_length=20, label="Phone Number")
    reason = forms.CharField(max_length=500, widget=forms.Textarea, label="Why do you want to attend the workshop?")
