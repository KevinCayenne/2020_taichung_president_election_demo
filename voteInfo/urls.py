from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from voteInfo import views

urlpatterns = [
    path('', views.result, name="home"),
    path('index/', views.index),
]
