from django.shortcuts import render
from loginapp.forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
def index(request):
    if not request.user.is_authenticated:
        return render(request,'loginapp/login.html')
    return render(request,'todolist/add_task.html')
@login_required
def special(request):
    return render(request,'todolist/add_task.html')
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
def register(request):
    if request.user.is_authenticated:
        return render(request,'todolist/add_task.html')
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
            msg="Registration Successfull"
            return render(request,'loginapp/registration.html',
                                {'user_form':user_form,
                               'registered':registered,
                               'msg' : msg})
        else:
            print(user_form.errors)
            msg=user_form.errors
            return render(request,'loginapp/registration.html',
                                {'user_form':user_form,
                               'registered':registered,
                               'msg': msg})
    else:
        user_form = UserForm()
        msg=""
        return render(request,'loginapp/registration.html',
                            {'user_form':user_form,
                           'registered':registered,
                           'msg': msg})
def user_login(request):
    if request.user.is_authenticated:
        return render(request,'todolist/add_task.html')
    success = False
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                success = True
                return HttpResponseRedirect(reverse('index'))
            else:
                msg="User Inactive"
                return render(request, 'loginapp/login.html', {"success" : success, "msg" : msg})
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            msg="Username or Password Invalid"
            return render(request, 'loginapp/login.html', {"success" : success, "msg" : msg})
    else:
        msg=""
        return render(request, 'loginapp/login.html', {"success" : success, "msg" : msg})
