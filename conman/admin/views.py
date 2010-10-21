from django.http import HttpResponse, HttpResponseRedirect
from ecell2.conman.core.models import Updates, Incubation
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import user_passes_test
import datetime
from ecell2.conman.admin import forms
from ecell2.conman.admin.models import *

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
        from messages import msg
        context.update({ 'msg' : msg[request.GET['msg_id']][1] ,
                         'msg_type' : msg[request.GET['msg_id']][0]})

    
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
                if post['published'] == '0':
                    i.published = False
                else:
                    i.published = True
            i.save()
            print Incubation.objects.get(pk=post['pk']).published
            context = {'qs':Incubation.objects.all(), 'type': 'incu'}
            return render_to_response('admin/qs_template.html', context )
    else:
        # if request is GET
        context = {'qs':Incubation.objects.all(), 'type': 'incu'}
        return render_to_response('admin/qs_template.html', context)

@user_passes_test(user_auth, login_url = '/not_allowed/')
def change(request, data_type):
    import internals
    handler = internals.handlers.get(data_type, None) 
    
    if request.method == "GET":
        context = {'qs':handler.get('model').objects.all(), 'type':data_type}
        return render_to_response('admin/display_table.html', context)
    else:
        # request is POST
        post = request.POST.copy()
        if post['pk'] == 0: 
            # 0 corresponds to request for a new entry
            entry = handler.get('model')(post) 
            entry.save()
            return HttpResponseRedirect('/admin?msg_id=2#'+data_type)
        else:
            # corresponds to request for change in entry.
            return HttpResponse("lajsdlfjalkdjf")


def form(request, data_type):
    import internals
    handler = internals.handlers.get(data_type, None)
    
    if request.method == "GET":
        context = {'form':handler.get('form')(), 'formfor' : data_type}
        return render_to_response('admin/display_form.html', context)


@user_passes_test(user_auth, login_url = '/not_allowed/' )
def massmail(request):
    context = getBaseContext(request)
    if request.method == 'GET':
        mlf = forms.MailListForm()

        context.update({'mlf':mlf})
        return render_to_response('admin/mail_sender.html', context)

    elif request.method == 'POST':
        post = request.POST.copy()
        mailer = Mailer(content = post['content'],
                      subject = post['subject'],
                      user = request.user,
                      from_field = post['from_field'],
                      )
        mailer.save()
        #mail.to = request.POST.getlist('mList')

        import mail

        for item in request.POST.getlist('mList'):
            mail.MailThread(mailer, item, 0.5).start()

        return HttpResponseRedirect('/admin/')

