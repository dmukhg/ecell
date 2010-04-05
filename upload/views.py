from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from forms import *
import models
from definitions import *

def upload(request):
    if request.method=="POST":
        if request.user.is_authenticated():
            user=request.user
            form = UploadForm(request.POST, request.FILES) 
            if form.is_valid():
                u = models.upload(get_file=request.FILES['get_file'],
                            uploaded_by=request.user,
                            access_level=PUBLIC,
                            uploaded_for="frontend")
                u.save()
                return HttpResponseRedirect("/upload")
            else:
                return render_to_response("upload.html",{"form":form})




    else:
        return render_to_response("upload.html",{'form':UploadForm()})



