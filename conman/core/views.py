from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from ecell2.conman.core.models import *
from ecell2.root_views import get_base_vars 

def home(request):
    base_vars = get_base_vars(request)
    
    # fetching updates and snippets
    updates = Updates.objects.all().filter( active = True ).order_by( 'date' )[:4]
    snippets = Snippets.objects.all().order_by( 'pk' )[:4] 

    # adding updates to the template dict
    base_vars.update({'updates':updates})
    base_vars.update({'snippets':snippets})
    return render_to_response("home.html", base_vars  )


def article(request,url):
    base_vars = get_base_vars(request)
    url_bak = url

    # stripping url of trailing /
    # neccessary in case a url like /initiativse/kljsaf/lsfjdsl/// is entered
    url = url.split('/')
    while url[-1] is u'':
       del(url[-1])

    if url.__len__() is 1:
        '''Do whatever for top level elements'''
        sector = Sector.objects.get( url =url.pop() , parent = None )
    else:
        '''Return the article matching the given sector and pass it to the template with the updated base_var dictionary'''
        sector = Sector.objects.get( url = url.pop() , parent = Sector.objects.get( url = url.pop()))

    # generating article content & heading
    heading = sector.name
    text = sector.article.content

    # generating breadcrumbs
    crumbs = [sector]
    while crumbs[-1].parent is not None:
        crumbs.append( crumbs[-1].parent )
    crumbs.reverse()

    # generating top_nav level 2
    current_root_sector = crumbs[0] 

    # generating sidebar
    siblings = Sector.objects.filter( parent = sector.parent )
    children = Sector.objects.filter( parent = sector )

    base_vars.update({'article':text,'heading':heading, 'url' : url_bak , 'crumbs' : crumbs , 'siblings' : siblings , 'children' : children , 'current_root_sector' : current_root_sector })
    return render_to_response("article.html", base_vars)

    # Otherwise return Http404 since no match could be found
    return render_to_response("404.html",base_vars)


def pages(request, url):
    base_vars = get_base_vars(request)

    try:
        page = Page.objects.get( url=url )
        url = 'page/%s' %url
    except:
        page = Page.objects.get( pk=1 ) 
        url = ''
    base_vars.update({'page' : page, 'url' : url })
    return render_to_response('pages.html', base_vars)

import forms
def pre_reg_entry(request):
    print '1'
    if request.method == "POST":
        print '2'
        form_ = forms.PreRegForm(request.POST)
        if form_.is_valid():
            print "SUccess"
            entry = Pre_reg_entry(
                    name=request.POST['name'],
                    rollno=request.POST['rollno'],
                    email=request.POST['email'],
                    phno=request.POST['phno'],
                    reason=request.POST['reason']
                    )
            entry.save()
            return HttpResponseRedirect('/workshop?success=true')
        else:
            print '3'
            return render_to_response('reg_entry.html', {'form':form_})
    if request.method == 'GET':
        print '4'
        form_ = forms.PreRegForm()
        if request.GET.has_key('success'):
            print '6'
            success = True
        else:
            print '5'
            success = False
        return render_to_response('reg_entry.html' , {'form':form_, 'success':success})

def custom_view(request):
    entry_set = Pre_reg_entry.objects.all()
    return render_to_response('custom_view.html', {'qs':entry_set})
