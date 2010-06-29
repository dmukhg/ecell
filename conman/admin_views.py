from django.http import HttpResponseRedirect
from datetime import datetime
from django.shortcuts import render_to_response
from models import *
from forms import *

def index( request, message = None ):
    updates = Updates.objects.all()

    temp_vars = { 'updates' : updates ,
                    'message' : message, 
                    'user' : request.user ,
                    }

    return render_to_response('admin.html' , temp_vars )

def updates_delete( request , pk):
    if request.user.is_staff and request.user.is_authenticated():
        try:
            up = Updates.objects.get( pk = pk ) 
            up.active = False
            up.save()
        except:
            return index( request , message = "Couldn't process your request. Engineers have been informed" ) 
    return HttpResponseRedirect('/admin/')

def updates_add( request , pk = 0 ):
    if request.user.is_staff and request.user.is_authenticated():
        if request.method == 'POST':
            if pk == 0:
            # for adding an update
                up = Updates()
                up.date = datetime.today()
            else:
                try:
                    up = Updates.objects.get(pk = pk )
                except:
                    return index( request , message = "Couldn't process your request. Engineers have been informed" ) 
            up_form = UpdateForm( request.POST )
            if up_form.is_valid():
                up.description = request.POST['description']
                up.content = request.POST['content']
                up.url = request.POST['url']
                up.save()
                return index( request , message = "Succesfully added / edited update.")
            else:
                return render_to_response( 'admin_form.html' , {'form' : up_form } )

        if request.method == 'GET':
            if pk == 0:
                up_form = UpdateForm()
            else:
                try:
                    up = Updates.objects.get(pk = pk )
                    up_form = UpdateForm( up.__dict__ ) 
                except:
                    return index( request , message = "Couldn't process your request. Engineers have been informed" ) 
            return render_to_response( 'admin_form.html' , { 'form' : up_form } )
    else:
        return HttpResponseRedirect('/admin/')

def sector_add( request , pk = 0):
    return render_to_response( "admin_form.html" ,{ 'form' : SectorForm() })
