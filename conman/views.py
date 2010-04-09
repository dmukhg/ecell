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

    return render_to_response("home.html",{'logged':logged,'tabsList':tabs_qs,'foot_pool':foot_pool})

