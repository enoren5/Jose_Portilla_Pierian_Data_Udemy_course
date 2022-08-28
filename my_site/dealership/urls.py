from django.http.response import HttpResponse
from django.urls import path, include
from . import views


app_name = 'dealership'
urlpatterns = [
    path('list/', views.list_view, name='list'),
    path('add/', views.add, name='add'),
    path('delete/', views.delete, name='delete'),
    
]
