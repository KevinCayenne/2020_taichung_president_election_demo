from django.shortcuts import render, redirect

def result(request):
    return render(request, "voteInfo/result.html")

def index(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    return render(request, "voteInfo/index.html")
