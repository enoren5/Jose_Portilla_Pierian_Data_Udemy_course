from django.http.response import HttpResponse
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.list_patients),
    
]
