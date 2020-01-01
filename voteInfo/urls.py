from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from voteInfo import views

urlpatterns = [
    path('', views.result),
    path('index/', views.index),
]
