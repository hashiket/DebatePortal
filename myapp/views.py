from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from .models import UsersType, DebateTopic
from django.contrib import messages




# Create your views here.
def index(request):
    topics = DebateTopic.objects.all()
    return render(request,"myapp/main.html",{'topics':topics})

def logout(request):
    auth.logout(request)
    return redirect('/')


def login(request):
    if request.method== 'POST':
        username=request.POST['username']
        password=request.POST['password']
        print(username)
        print(password)
        user=auth.authenticate(request,username=username,password=password)
        if user:
                auth.login(request,user)
                return redirect("debater")
        else:
            messages.info(request,"Invalid Credentials")
            return redirect("login")
    else:
        return render(request,"myapp/login.html")



def register(request):
    if request.method == 'POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        if password1==password2:
             if User.objects.filter(username=username).exists():
                   messages.info(request,'Username Taken')
                   return redirect('register')
             else:
                  user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,password=password1)
                  user.save();

                  us=UsersType(user=user,user_type="DU")
                  us.save();

                  print('user created')
                  return redirect('login')
        else:
            messages.info(request,'password not matching...')
            return redirect('register')
        return redirect('/')   
    else:
        return render(request,"myapp/register.html")

def adminlogin(request):
    return render(request,"myapp/adminlogin.html")

def admin(request):
    return render(request,"myapp/admin.html")

def addtopic(request):
    return render(request,"myapp/addtopic.html")

def alltopic(request):
    return render(request,"myapp/alltopic.html")

def alldebater(request):
    return render(request,"myapp/alldebater.html")

def debater(request):
    topics = DebateTopic.objects.all()
    return render(request,"myapp/debater.html",{'topics':topics})

def view(request):
    if request.method == 'POST':
        first_name=request.POST.get('first_name')
    else:
        return render(request,"myapp/view.html")