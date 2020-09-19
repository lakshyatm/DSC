from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, Http404
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .models import Kitty,Expense,Final
# Create your views here.

def home(request):
    
    if request.method == 'POST':
        nm = request.POST["event"]
        email = request.POST["peremail"]
        n1 = request.POST["per1"]
        n2 = request.POST["per2"]
        # input_names = [name for name in request.POST.keys() if name.startswith('vyakti-')]
        # for input_name in input_names:
        #     soft_name = request.POST["name"]
        #     print(soft_name)
        data = Kitty(event_name=nm,person1_email=email,person1=n1,person2=n2)
        data.save()
        return HttpResponseRedirect('second')

    return render(request,'home.html')

def second(request):
    g = Kitty.objects.last()
    n1=g.person1
    n2=g.person2

    if request.method == 'POST':
        se = request.POST["sel"]
        amt = request.POST["amount1"]
        #rad1 = request.POST["radio1"]
        #print(rad1)
        #rad2 = request.POST["radio2"]
        #print(rad2)
        exp = request.POST["expensename"]
        dt = request.POST["dtg"]

        # data = Expense(paid_person=se,amount=amt,split_equ_all=rad1,split_diff=rad2,exp_name=exp,date=dt)
        
        data = Expense(paid_person=se,amount=amt,exp_name=exp,date=dt)
        data.save()
        return HttpResponseRedirect('third')

    return render(request,'second.html',{'n1':n1,'n2':n2})

def third(request):
    e = Kitty.objects.last()
    n1 = e.person1
    n2 = e.person2
    d = Expense.objects.last()
    amt = d.amount

    
    # data = Final(paid_per=paid)
    # data.save()

    fi = d.paid_person

    if fi == n1:
        e2 = amt/2
        e3 = amt
        e4 = amt/2
    

    return render(request,'third.html',{'fi':fi,'n1':n1,'n2':n2,'e1':amt,'e2':e2,'e3':e3,'e4':e4})

def fourth(request):
    e = Kitty.objects.last()
    n1 = e.person1
    n2 = e.person2
    d = Expense.objects.last()
    amt = d.amount

    print("hello")
    
    e2 = amt/2
    e3 = 0
    e4 = amt/2

    return render(request,'third.html',{'n1':n2,'n2':n1,'e1':amt,'e2':e2,'e3':e3,'e4':e4})



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
