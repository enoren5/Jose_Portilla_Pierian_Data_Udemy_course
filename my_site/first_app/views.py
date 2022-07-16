from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def sports_view(request):
    return HttpResponse('Sports View!')

def finance_view(request):
    return HttpResponse('Finance View!')