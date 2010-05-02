from django.http import HttpResponse
from django.shortcuts import render_to_response
from models import *
from utils import FooterFormatter
from ecell2.root_views import get_base_vars

def home(request):
    base_vars = get_base_vars(request)
    
    updates = Updates.objects.all()[:4]

   
    base_vars.update({'updates':updates})
    return render_to_response("home.html", base_vars  )


def article(request,url):
    base_vars = get_base_vars(request)

    # stripping url of trailing /
    url = url.split('/')
    while url[-1] is u'':
       del(url[-1])

    if url.__len__() is 1:
       '''Do whatever for top level elements'''
       text = Sector.objects.get( url =url.pop() , parent = None )
       heading = text.name
       text = text.name
       
    else:
       text = Sector.objects.get( url = url.pop() , parent = Sector.objects.get( url = url.pop()))
       heading = text.name
       text = text.article

       base_vars.update({'article':text,'heading':heading})
       
       return render_to_response("article.html", base_vars)

   


    return render_to_response("404.html",base_vars)



