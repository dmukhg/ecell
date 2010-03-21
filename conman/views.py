from django.http import HttpResponse
from django.shortcuts import render_to_response
from ecell2.conman.models import *

def home(request):
	tabs_qs = Section.objects.all()
	print "Home"
	return render_to_response("base.html",{'tabsList':tabs_qs})

def article(request, article_request):
	tabs_qs = Section.objects.all()
        article=Article.objects.get(url=article_request)
	if not article :
		return render_to_response("404.html",{'tabsList':tabs_qs,})
	return render_to_response("article.html",{'tabsList':tabs_qs,'article':article})

