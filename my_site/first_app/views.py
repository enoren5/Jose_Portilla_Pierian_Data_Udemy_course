from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound, Http404

articles = {
    'sports':'Sports Page',
    'finance': 'Finance Page',
    'thelema': '93! “Love is the law, love under will.”',
}

def news_view(request, topic):
    try:
        result = articles[topic]
        return HttpResponse(articles[topic])
    except:
        raise Http404("404 Generic") 
        #return HttpResponseNotFound(result)

def addition_view(request, num1, num2):
    product = num1 ** num2
    output = f'{num1} exponent {num2} = {product}' 
    return HttpResponse(str(output))
