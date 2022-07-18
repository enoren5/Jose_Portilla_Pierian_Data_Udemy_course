from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

my_var = {
        'first_name': 'aleister',
        'last_name': 'crowley',
        'author_list': ['Paul F. Case','Arthur E. Waite','Manly P. Hall','Aleister Crowley',],
        'some_dict': {'inside_key':'inside_value'},
        'user_logged_in': False,
        'some_letter_list': ['a','b','c','d','e','f','g','h','i']
        }

def example_view(request):
    #my_app/templates/my_app/example.html
    return render(request, 'my_app/example.html')

def variable_view(request):
    return render(request,'my_app/variable.html', context=my_var)