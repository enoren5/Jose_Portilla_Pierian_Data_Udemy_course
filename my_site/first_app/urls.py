from django.urls import path
from . import views

urlpatterns = [
    path('<str:topic>/', views.news_view, name='topic-page'),
    path('<int:num1>/<int:num2>', views.addition_view),
    path('<int:num_page>',views.num_page_view),
]