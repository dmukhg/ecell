from django.http import HttpResponse
from django.shortcuts import render_to_response
from models import *
from utils import FooterFormatter

def home(request):
    logged = request.user.is_authenticated()
    tabs_qs = Sector.objects.filter(parent=None).order_by('display_order')
    footer_qs = FooterFormatter(Sector.objects.all())
    foot = footer_qs[0]
    sub_foot = footer_qs[1]

    foot_pool = {}

    for (k,v) in zip(foot,sub_foot):
        foot_pool[k] = v


    updates = Updates.objects.all()[:4]

    return render_to_response("home.html",{'logged':logged,'tabsList':tabs_qs,'updates':updates,'foot_pool':foot_pool})


def article(request,url): ###Eunikorn - rewritten with major changes
    logged = request.user.is_authenticated()
    tabs_qs = Sector.objects.filter(parent=None).order_by('display_order')
    footer_qs = FooterFormatter(Sector.objects.all())
    foot = footer_qs[0]
    sub_foot = footer_qs[1]

    foot_pool = {}

    for (k,v) in zip(foot,sub_foot):
        foot_pool[k] = v

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
       return render_to_response("article.html", {"article":text,"heading":heading,"logged":logged,"tabsList":tabs_qs,"foot_pool":foot_pool})

   


    return render_to_response("404.html",{'logged':logged,'tabsList':tabs_qs,'foot_pool':foot_pool})



