from django.contrib import admin
from django.http.response import HttpResponse
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('first_app/',include('first_app.urls')),
    path('my_app/',include('my_app.urls')),
    path('', include('office.urls'))
]

handler404 = 'my_site.views.my_custom_page_not_found_view'