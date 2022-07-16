from django.shortcuts import render
from django.http import HttpResponse

articles = {
    'sports':'Sports Page',
    'finance': 'Finance Page',
    'thelema': 'Thelemic Page',
}

def sports_view(request):
    return HttpResponse(article[thelema])

def finance_view(request):
    return HttpResponse(article[finance])