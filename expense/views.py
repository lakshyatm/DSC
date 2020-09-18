from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, Http404
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
# Create your views here.

def home(request):
    return render(request,'home.html')


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request,user)
                    return render(request,'home.html')
                else:
                    return HttpResponse("User is not active")
            else:
                return HttpResponse("User is None")
    else:
        form = UserLoginForm()

    context = {
        'form':form,
    }
    return render(request,'login.html',context)


def user_logout(request):
    logout(request)
    return render(request,'home.html')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST or None)
        if form.is_valid:
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return redirect('user_login')
    else:
        form = UserRegistrationForm()
    context ={
        'form':form,
    }
    return render(request, 'register.html',context)
