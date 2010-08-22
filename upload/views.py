from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from ecell2.upload.forms import *
from ecell2.upload import models
from ecell2.upload.definitions import *

def upload(request):
    '''Incomplete for now copy image_upload code
    that works and add whatever is nessessary for
    outsiders'''
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
                return render_to_response("upload.html",{"heading":"File Upload","form":form})
    else:
        return render_to_response("upload.html",{"heading":"Upload File",'form':UploadForm()})


def image_upload( request ):
    if request.method == "POST":
        if request.user.is_authenticated() and request.user.is_staff:
            user = request.user
            form = ImageForm( request.POST , request.FILES )
            if form.is_valid():
                u = models.image( file = request.FILES['get_image'] )
                u.save()
                return render_to_response( "upload.html" , {"heading":"Upload Successful any more:", "form":ImageForm()}) 
            else:
                return render_to_response( "upload.html" , {"heading":"Image Upload","form":form})
        else:
            return render_to_response( "message.html" , {"message":"Hey! get out of here. You are not authorised to do whatever it is that you are trying. Login as a staff member to get this service" })
    else:
        return render_to_response("upload.html", {"heading":"Image Upload", "form":ImageForm()})
