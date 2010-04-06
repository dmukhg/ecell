from django.http import HttpResponse
from django.shortcuts import render_to_response
from ecell2.conman.models import *

def home(request):
	tabs_qs = Sector.objects.filter(parent=None).order_by('display_order')
	return render_to_response("base.html",{'tabsList':tabs_qs})

