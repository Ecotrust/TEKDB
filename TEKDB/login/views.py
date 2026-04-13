# Create your views here.
from django.http.response import JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.views import PasswordChangeView, update_session_auth_hash


def index(request):
    context = {
        "pageTitle": "Login",
    }
    return render(request, "index.html", context)


def login(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        auth_login(request, user)
        from explore.views import explore

        return explore(request)
    else:
        context = {
            "errorcode": 403,
            "error": "User name or password incorrect.",
            "page": "error",
            "pageTitle": "Error",
            "pageContent": "<p>There was an error with your request. Please see below for details.</p>",
            "user": request.user,
        }
        return render(request, "error.html", context)


def login_logic(request, context={}):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(username=username, password=password)
    if user is not None:
        auth_login(request, user)
        context = {
            "success": True,
            "username": user.username,
        }
        return context
    else:
        context = {
            "success": False,
        }
        return context


def login_async(request):
    login_user = login_logic(request)  # run default logic
    context = {
        "success": login_user["success"],
    }
    return JsonResponse(context)


class PasswordChangeView(PasswordChangeView):
    def form_valid(self, form):
        self.object = form.save()
        # prevent user’s auth session to be invalidated
        # and user have to log in again after password change
        update_session_auth_hash(self.request, self.object)
        return JsonResponse({"data": form.is_valid()}, status=200)
