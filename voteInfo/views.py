from django.shortcuts import render

# Create your views here.
import pyrebase
import firebase_admin
from django.shortcuts import render
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("president_vote_sdk.json")

# 初始化firestore
firebase_admin.initialize_app(cred)

def index(request):
    return render(request, "voteInfo/index.html")

def singIn(request):
    return render(request, "voteInfo/signIn.html")

def postsign(request):
    email = request.POST.get('email')
    passw = request.POST.get("pass")
    try:
        user = auth.sign_in_with_email_and_password(email,passw)
    except:
        message = "invalid cerediantials"
        return render(request, "voteInfo/signIn.html",{"msg":message})
    print(user)
    return render(request, "voteInfo/welcome.html",{"e":email})
