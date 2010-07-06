from django.http import HttpResponse
from conman.core.models import Updates
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import user_passes_test
import datetime

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



# HTTP views begin here 


@user_passes_test( user_auth , login_url = '/not_allowed/' )
def index( request ):
    update_list = Updates.objects.all()
    context = { 'update_list' : update_list }

    return render_to_response( 'admin/base.html' , context )


@user_passes_test( user_auth , login_url = '/not_allowed/' )
def create_update( request ):
    errors = []
    return_response = {}
    if request.method == 'POST':
        post = request.POST.copy()
        if post.has_key( 'description' ) and post.has_key( 'content' ) and post.has_key( 'url' ):
            Updates.objects.create( description = post['description'],
                           content = post['content'],
                           date = datetime.date.today(),
                           url = post['url'],
                           )
            return HttpResponse( 'success' )
        else:
            if not post.has_key( 'description' ):
                errors.append( 'You need to enter a description.' )
            if not post.has_key( 'url' ):
                errors.append( 'You need to enter a valid url.' )
            if not post.has_key( 'content' ):
                errors.append( 'You need to enter some content.' )
             
    else:
        # request method is GET
        return None
