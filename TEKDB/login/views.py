# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login

def index(request):
    context = {
        "pageTitle": "Login",
    }
    return render(request, "index.html", context)
    #return HttpResponse("<h1>Server error: Already Logged In")

def forgot(request):
    context = {
        "pageTitle": "Forgot Login",
    }
    return render(request, "forgot.html", context)
    #return HttpResponse("<h1>Forgot Password")

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        auth_login(request, user)
        from explore.views import explore
        return explore(request)
    else:
        context = {
            "errorcode": 403,
            "error": "User name or password incorrect.",
            'page':'error',
            'pageTitle':'Error',
            'pageContent':"<p>There was an error with your request. Please see below for details.</p>",
            'user': request.user
        }
        return render(request, "error.html", context)
