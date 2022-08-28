from django.http.response import HttpResponse
from django.urls import path, include
from . import views

app_name = 'car_rentals'
urlpatterns = [
    path('', views.rental_review, name='rental_review'),
    path('thank_you/', views.thank_you, name='thank_you'),    
]