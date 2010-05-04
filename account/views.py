from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from ecell2.root_views import get_base_vars
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth import logout as auth_logout
import models as account_models
from forms import *

def index(request):
    base_vars = get_base_vars(request)

    if request.user.is_authenticated():
        # doesn't need to signup
		return HttpResponseRedirect("/account/settings/")
    if request.method=="POST":
    # verify fields and login
        login_form = LoginForm( request.POST )
        if login_form.is_valid():
            email=request.POST['email']
            username=User.objects.get(email=email)
            password=request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                # authenticated so returning as authenticated
                login(request,user)
                return HttpResponseRedirect("/");
            else:
                # error page with retry
                base_vars.update({"reg_form":SignupForm(),"login_form":LoginForm()})
                return render_to_response("account_login_register.html",base_vars) 
        else:
            base_vars.update({"reg_form":SignupForm(), "login_form":login_form})
            return render_to_response("account_login_register.html", base_vars)
    else:
        # if method is get returns login form 
        base_vars.update({"reg_form":SignupForm(),"login_form":LoginForm()})
        return render_to_response("account_login_register.html",base_vars)


def signup(request):
    base_vars = get_base_vars(request)

    if request.user.is_authenticated():
    # cant allow a logged in user to signup
        base_vars.update({"message":"You are already logged in. Please logout and then signup for a new account"})
        return render_to_response("message.html",base_vars)
    else:
        if request.method=="POST":
        # Submission 
            suForm=SignupForm(request.POST)
            if suForm.is_valid():
                pk=len(User.objects.all()).__str__()
                username=pk.join([request.POST['first_name'],request.POST['last_name']])
                user=User.objects.create_user(username=username,email=request.POST['email'],password=request.POST['password1']) #create a User with the given name as username and password 
                user.first_name=request.POST['first_name']
                user.last_name=request.POST['last_name']
                user.save()
                #save the other credentials of the Person
                person = account_models.person()
                person.user_ptr = user
                person.sex = request.POST['sex']
                person.occupation = request.POST['occupation']
                person.phno = request.POST['phno']
                person.institution = request.POST['institution']
                person.address = request.POST['address']
                person.pin = request.POST['pin']
                person.save()
                # log him in and go to home page
                logged_in_user = authenticate(username=username,password=request.POST['password1'])
                if logged_in_user is not None:
                    login(request,logged_in_user)
                    return HttpResponseRedirect("/")        
            else:
			    # invalid form
                base_vars.update({"reg_form":suForm,"login_form":LoginForm()})
                return render_to_response("account_login_register.html",base_vars)
        else:
        # unauthenticated user so return a blank form
            base_vars.update({"reg_form":SignupForm(),"login_form":LoginForm()})
            return render_to_response("account_login_register.html",base_vars)

def settings(request):
    base_vars = get_base_vars(request)
    try:
        pwdChng=request.GET['pwdChng']
        if pwdChng == 'Success':
            base_vars.update({'pwdMsg':"<span style='color:#008800'>Password Change Successful</span>"})
        elif pwdChng == "Fail":
            base_vars.update({'pwdMsg':"<span style='color:#880000'>Password Change Fail</span>"})

                    
    except:
        pass

    if request.user.is_authenticated():
        user_current=User.objects.get(email=request.user.email)
        person_current=account_models.person.objects.get(user_ptr=user_current.pk)
        user_data={}
        user_data['first_name']=user_current.first_name
        user_data['last_name']=user_current.last_name
        user_data['sex']=person_current.sex
        user_data['occupation']=person_current.occupation
        user_data['phno']=person_current.phno
        user_data['institution']=person_current.institution
        user_data['address']=person_current.address
        user_data['pin']=person_current.pin

        pool=AccountSettingsForm(user_data)
        base_vars.update({'pool':pool})	
        return render_to_response("account_settings.html",base_vars)
    else:
        base_vars.update({"reg_form":SignupForm,"login_form":LoginForm()})
        return render_to_response("account_login_register.html",base_vars)

def logout(request):
    if request.user.is_authenticated():	
        auth_logout(request)
        return HttpResponseRedirect("/")
    else:
        base_vars = get_base_vars(request)

    base_vars.update({"message":"You are not authorised to be here"})
    return render_to_response("message.html", base_vars)

                    
def change(request):
    if request.user.is_authenticated() and request.method == "POST":
        user = request.user
        person = account_models.person.objects.get( user_ptr = user )
        # assignments follow
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.save()

        person.occupation = request.POST['occupation']
        person.phno = request.POST['phno']
        person.institution = request.POST['institution']
        person.address = request.POST['address']
        person.pin = request.POST['pin']
        person.save()

        return HttpResponseRedirect('/account/settings')

    else:
        base_vars = get_base_vars(request)

        base_vars.update({"message":"You are not authorised to be here"})
        return render_to_response("message.html", base_vars)


def change_password(request):
    if request.user.is_authenticated() and request.user.check_password( request.POST['old_pass'] ):
        user=request.user
        user.set_password(request.POST['new_pass'])
        user.save()
    
    else:
        return HttpResponseRedirect('/account/settings?pwdChng=Fail')

    return HttpResponseRedirect('/account/settings?pwdChng=Success')

