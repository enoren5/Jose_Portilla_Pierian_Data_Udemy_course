from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def example_view(request):
    #my_app/templates/my_app/example.html
    return render(request, 'my_app/example.html')