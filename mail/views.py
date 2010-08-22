from django.http import HttpResponse, HttpResponseRedirect
from ecell2.mail.models import *
from django.shortcuts import render_to_response
from ecell2.conman.admin.views import user_auth, superuser_auth
from django.contrib.auth.decorators import user_passes_test
from django.core.mail import send_mail, EmailMultiAlternatives

@user_passes_test(user_auth, login_url='/page/not_allowed')
def index(request):
    if request.method == 'GET':
        return render_to_response('mail_sender.html')
    elif request.method == 'POST':
        post = request.POST.copy()
        mail = Mailer(content = post['content'],
                      subject = post['subject'],
                      user = request.user,
                      from_field = post['from_field'])
        mail.save()

        list = ['dipanjan.mu@gmail.com',] 
        for id in list:
            msg = EmailMultiAlternatives(mail.subject,'','',mail.from_field,[id])
            msg.attach_alternative(mail.content,"text/html")
            msg.send()

        return HttpResponse("Mail sent!")

