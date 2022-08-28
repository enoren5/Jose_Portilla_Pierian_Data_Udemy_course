from django.shortcuts import render

# Create your views here.

def list_view(request):
    return render(request, 'dealership/list.html')

def delete(request):
    return render(request, 'dealership/delete.html')

def add(request):
    return render(request, 'dealership/add.html')