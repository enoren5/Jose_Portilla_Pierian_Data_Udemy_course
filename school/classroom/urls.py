from django.urls import path
from .views import home_view, HomeView, ThankYouView

app_name = 'classroom'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('thanks/', ThankYouView.as_view(), name='thanks')
]