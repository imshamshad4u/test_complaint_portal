from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import Group


def unauthenticated_user(view_func):
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_authenticated():
            return redirect('home')
        else:
            return view_func(request,*args,**kwargs)
    return wrapper_func


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request,*args,**kwargs):
            group=None
            print("working",allowed_roles)
            print("which group",request.user.groups.exists())
            print("decorator user",request.user)
            if request.user.groups.exists():
                group=request.user.groups.all()[0].name
                print("group",group)
            if group in allowed_roles:
                return view_func(request,*args,**kwargs)
            else:
                print("group",group)

                return HttpResponse("You are not authorized to view this page")
        return wrapper_func
    return decorator
def user_belongs_to_admin_group(user):
    admin_group = Group.objects.get(name='admin')
    return admin_group in user.groups.all()