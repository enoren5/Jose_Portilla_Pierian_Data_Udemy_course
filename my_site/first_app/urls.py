from django.urls import path
from . import views

urlpatterns = [
    path('sports_view/', views.sports_view),
    path('finance_view/', views.finance_view)
]