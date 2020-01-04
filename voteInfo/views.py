from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import models

def result(request):
    return render(request, "voteInfo/result.html")

def index(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')

    user = models.User.objects.get(username=request.user)
    return render(request, "voteInfo/index.html", {'password': user.password})

def dept(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')

    user = models.User.objects.get(username=request.user)
    return render(request, "voteInfo/dept.html", {'password': user.password})
