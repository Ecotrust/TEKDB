from django.http.response import JsonResponse
from django.shortcuts import render
from django.contrib.auth import (
    authenticate,
    login as auth_login,
    update_session_auth_hash,
)
from django.contrib.auth.views import PasswordChangeView


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


class TEKDBPasswordChangeView(PasswordChangeView):
    def form_invalid(self, form):
        return JsonResponse({"data": form.errors, "success": False}, status=400)

    def form_valid(self, form):
        self.object = form.save()
        # prevent user’s auth session to be invalidated
        # and user have to log in again after password change
        update_session_auth_hash(self.request, self.object)
        return JsonResponse({"data": None, "success": True}, status=200)
