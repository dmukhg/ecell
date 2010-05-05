from django.http import HttpResponse
from django.shortcuts import render_to_response
from models import *
from utils import FooterFormatter
from ecell2.root_views import get_base_vars

def home(request):
    base_vars = get_base_vars(request)
    
    # fetching updates
    updates = Updates.objects.all()[:4]

    # adding updates to the template dict
    base_vars.update({'updates':updates})
    return render_to_response("home.html", base_vars  )


def article(request,url):
    base_vars = get_base_vars(request)
    url_bak = url

    # stripping url of trailing /
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

    base_vars.update({'article':text,'heading':heading, 'url' : url_bak , 'crumbs' : crumbs })
    return render_to_response("article.html", base_vars)

    # Otherwise return Http404 since no match could be found
    return render_to_response("404.html",base_vars)



