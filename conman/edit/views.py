from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from conman.models import *
from ecell2.root_views import get_base_vars

def edit_article(request , url ):
    base_vars = get_base_vars(request)
    url_bak = url

    if not request.user.is_staff:
        base_vars.update({'message':'You are not authorised to edit articles. You must login as a staff member to do that.'})
        return render_to_response("message.html", base_vars )

    # check whether home page has been requested
    if url == u'/' or url == u'':
        base_vars.update({"message":"You cannot edit the home page. You need superuser access. Contact your sysadmin."})
        return render_to_response("message.html", base_vars)
 

    # stripping url of trainling /
    url = url.split('/')

    while url[-1] is u'':
        del(url[-1])

    # processing url_bak to make it point to article
    url_bak = url_bak.split('/')
    url_bak = [ item for item in url_bak if not ( ( item == u'edit') or (item == u'submit') )]
    url_bak = '/'.join( url_bak )

    if request.method == "GET":
        print url;
        if url.__len__() is 2:
            '''top level'''
            text = Sector.objects.get( url = url.pop() , parent = None )
            heading = text.name
            text =text.article.content

        else:
            '''not top level'''
            text = Sector.objects.get( url = url.pop() , parent = Sector.objects.get( url = url.pop() ) )
            heading = text.name
            text = text.article.content
    
        base_vars.update({'article':text, 'heading': heading, 'url': url_bak })
        return render_to_response("editor.html" , base_vars)
    
    

    elif request.method == "POST":
        text = request.POST['elm1']
        if url.__len__() is 3: # since u'submit' also in url
            ''' top level '''
            article = Sector.objects.get( url = url.pop() , parent = None ) 
        else:
            ''' not top level '''
            article = Sector.objects.get( url = url.pop() , parent = Sector.objects.get( url = url.pop() ) )
        article = article.article
        article.content = text
        article.save()

        return HttpResponseRedirect(url_bak)
