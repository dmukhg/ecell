from conman.models import *
from django.contrib.auth.models import AnonymousUser

def get_base_vars(request):
    logged = request.user.is_authenticated()
    tabs_qs = Sector.objects.filter(parent = None).order_by('display_order')
    footer_qs = FooterFormatter(Sector.objects.all())
    foot = footer_qs[0]
    sub_foot = footer_qs[1]

    foot_pool = {}

    for (k,v) in zip (foot, sub_foot):
        foot_pool[k] = v

    # Check for staff access
    if request.user.is_anonymous():
        staff = False
        user = None
    else:
        staff = request.user.is_staff
        user = request.user.email

    result ={'logged':logged,
            'tabsList':tabs_qs,
            'foot_pool':foot_pool,
            'user':user,
            'staff':staff,}

    return result

def FooterFormatter(qs):
    foot = qs.filter(parent = None)
    sub_foot = []
    for item in foot:
        sub_foot.append(qs.filter(parent=item))
    result = (foot,sub_foot)
    return result
