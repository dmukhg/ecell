from django.http import HttpResponse, HttpResponseRedirect
from ecell2.conman.core.models import Updates, Incubation
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import user_passes_test
import datetime
from ecell2.conman.admin import forms
from ecell2.conman.admin.models import *
from django.core.mail import send_mail, EmailMultiAlternatives

# Defining decorators and other generic functions
def user_auth(user):
    try:
        if user.is_authenticated() and user.is_staff:
            return True
        return False
    except:
        return False


def superuser_auth(user):
    if user.is_authenticated() and user.is_superuser:
        return True
    return False


def getBaseContext(request):
    context = {}
    context['user'] = request.user.email
    context['su'] = request.user.is_superuser
    return context


# HTTP views begin here 
@user_passes_test(user_auth, login_url='/not_allowed/')
def index(request):
    context = getBaseContext(request)
    context.update({'incu_qs':Incubation.objects.all()})
    if request.GET.has_key('msg_id'):
        context.update({'msg':"Successful entry of incubation"})

    
    return render_to_response('admin/home.html', context) 

@user_passes_test(user_auth, login_url = '/not_allowed/' )
def incu(request):
    if request.method == "POST":
        post = request.POST.copy()
        if post['pk'] == '0':
            i = Incubation(name=post['name'], description=post['desc'])
            i.save()
            return HttpResponseRedirect('/admin?msg_id=2')
        else:
            i = Incubation.objects.get(pk=post['pk'])
            i.name = post.has_key('name') and post['name'] or i.name
            i.descrition = post.has_key('desc') and post['desc'] or i.description
            if post.has_key('published'):
                print post['published'] == '0'
                i.published = post['published'] == '0' and False or True
            i.save()
            print Incubation.objects.get(pk=post['pk']).published
            return HttpResponse('successs')
    return index(request)



@user_passes_test(user_auth, login_url = '/not_allowed/' )
def massmail(request):
    context = getBaseContext(request)
    if request.method == 'GET':
        mlf = forms.MailListForm()

        context.update({'mlf':mlf})
        return render_to_response('admin/mail_sender.html', context)

    elif request.method == 'POST':
        post = request.POST.copy()
        mail = Mailer(content = post['content'],
                      subject = post['subject'],
                      user = request.user,
                      from_field = post['from_field'],
                      )
        mail.save()
        #mail.to = request.POST.getlist('mList')

        mList = []

        for item in MailList.objects.all():
            if u'%d' %item.pk in request.POST.getlist('mList'):
                mList += ( eval('[%s]' % item.mList ) )

        finalList = []
        for _ in mList:
            ind = mList.index(_)
            if ind%100 ==0:
                finalList.append([])
            finalList[ind/100].append(_)
        import pprint
        print finalList

        for smallList in finalList:
            for _ in smallList:
                msg = EmailMultiAlternatives(mail.subject,
                                            "",
                                            mail.from_field,
                                            [_])
                msg.attach_alternative(mail.content,'text/html')
                msg.send()

        return HttpResponseRedirect('/admin/')
