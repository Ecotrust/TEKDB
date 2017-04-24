# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	return render(request, "index.html", {})
	#return HttpResponse("<h1>Server error: Already Logged In")

def forgot(request):
	return render(request, "forgot.html", {})
	#return HttpResponse("<h1>Forgot Password")

def create(request):
	return render(request, "create.html", {})
	#return HttpResponse("<h1>Create Password")

def logout(request):
	return HttpResponse("<h1>You have Logged Out")
