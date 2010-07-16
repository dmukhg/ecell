from django.http import HttpResponse
from ecell2.conman.core.models import Updates
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import user_passes_test
import datetime
import forms

# Defining decorators and other generic functions
def user_auth( user ):
    try:
        if user.is_authenticated() and user.is_staff:
            return True
        return False
    except:
        return False

def superuser_auth( user ):
    if user.is_authenticated() and user.is_superuser:
        return True
    return False

def getBaseContext( request ):
    context = {}
    context['user'] = request . user . email
    context['su'] = request . user . is_superuser

    return context



# HTTP views begin here 


@user_passes_test( user_auth , login_url = '/not_allowed/' )
def index( request ):
    context = getBaseContext( request )
    return render_to_response( 'admin/home.html' , context )

@user_passes_test( user_auth , login_url = '/not_allowed/' )
def updates( request ):
    context = getBaseContext( request )
    context['update_list'] = Updates.objects.all().order_by( 'date' )[:20]
    context['update_form'] = forms.UpdateForm()

    return render_to_response( 'admin/updates.html' , context )


@user_passes_test( user_auth , login_url = '/not_allowed/' )
def manage_update( request ):
    if request.method == 'POST' :
        post = request.POST.deepcopy()
        if post [ 'pk' ] != 0 :
            upd = Updates.objects.get( pk = post [ 'pk' ] )
                
    else:
        # request is GET
        return HttpResponse( 'Hey GET is not Allowed here' )

