from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"myapp/main.html")

def login(request):
    return render(request,"myapp/login.html")

def adminlogin(request):
    return render(request,"myapp/adminlogin.html")

def register(request):
    return render(request,"myapp/register.html")


def admin(request):
    return render(request,"myapp/admin.html")

def addtopic(request):
    return render(request,"myapp/addtopic.html")

def alltopic(request):
    return render(request,"myapp/alltopic.html")

def alldebater(request):
    return render(request,"myapp/alldebater.html")

def debater(request):
    return render(request,"myapp/debater.html")

def view(request):
    return render(request,"myapp/view.html")