# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

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

def create(request):
    context = {
        "pageTitle": "Create Account",
    }
    return render(request, "create.html", context)
    #return HttpResponse("<h1>Create Password")

def logout(request):
    return HttpResponse("<h1>You have Logged Out")
