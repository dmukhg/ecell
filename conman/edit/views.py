from django.http import HttpResponse, HttpResponseRedirect
from datetime import date
from django.shortcuts import render_to_response
from ecell2.conman.core.models import *
from ecell2.root_views import get_base_vars

def edit(request, url):
    # checking authorisation
    if request.user.is_authenticated() and request.user.is_staff:
        pass
    else:
        return HttpResponseRedirect( '/page/not-authorised' )

    # remove trailing '/'
    url = '/' + url.strip('/') 
    # figure out what is to be edited.
    calculated_type = url.split('/')[1]
   
    try:
        if calculated_type == 'page':
            editable = Page.objects.get( url=url.split('/')[2] )
            title = editable.title
            responseURL = '/' + '/'.join( url.split('/')[1:] )
        elif calculated_type == 'article':
            responseURL = '/' + '/'.join( url.split('/')[2:] )
            for sec in  Sector.objects.all():
                if sec.get_url() == responseURL:
                    editable = sec.article 
                    break
            title = sec.name
            editable.date = date.today()
        else:
            return HttpResponseRedirect('/page/page-not-found' )
    except:
        return HttpResponseRedirect('/page/non-existent-page' )

 
    # actual GET stuff  
    if request.method == "GET":
        base_vars = { 'editable' : editable.content,
                      'title' : title,
                      'url' : url }

        return render_to_response( 'editor.html', base_vars )

    if request.method == "POST":
        editable.content = request.POST['elm1']
        editable.save()
        return HttpResponseRedirect(responseURL) 


