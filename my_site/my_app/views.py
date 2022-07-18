from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def example_view(request):
    #my_app/templates/my_app/example.html
    return render(request, 'my_app/example.html')

def variable_view(request):
    my_var = {
        'first_name': 'Aleister',
        'last_name': 'Crowley',
        'author_list': ['Paul F. Case','Arthur E. Waite','Manly P. Hall',],
        'some_dict': {'inside_key':'inside_value'},
        }
    return render(request,'my_app/variable.html', context=my_var)