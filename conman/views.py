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


def article(request,article): ###Eunikorn - rewritten with major changes
    logged = request.user.is_authenticated()
    tabs_qs = Sector.objects.filter(parent=None).order_by('display_order')
    footer_qs = FooterFormatter(Sector.objects.all())
    foot = footer_qs[0]
    sub_foot = footer_qs[1]

    foot_pool = {}

    for (k,v) in zip(foot,sub_foot):
        foot_pool[k] = v


    pathComponents = article.split('/')
    print pathComponents 
    parent1 = None 
    for i in range(0,len(pathComponents)):
        try : 
            parent1 = Sector.objects.get(parent = parent1,url = pathComponents[i])
        except: ###Eunikorn : is there a need to check for MultipleObjectsReturned ? i dont think so 
            return render_to_response("404.html",{'tabsList':tabs_qs,'logged':logged,'foot_pool':foot_pool})
    #article = parent1.article

    return render_to_response("article.html",{'logged':logged,'tabsList':tabs_qs,'article':parent1.name,'pathComponents':pathComponents,'foot_pool':foot_pool})
