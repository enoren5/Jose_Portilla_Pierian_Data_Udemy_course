from django.shortcuts import render, redirect
from django.urls import reverse
from . import models

# Create your views here.

def list_view(request):
    all_vehicles = models.Vehicle.objects.all()
    context = {'vehicles':all_vehicles}
    return render(request, 'dealership/list.html', context=context)

def add(request):
    if request.POST:
        brand = request.POST['brand']
        year = int(request.POST['year'])
        models.Vehicle.objects.create(brand=brand, year=year)
        # After users submits car, redirect to list.html
        return redirect(reverse('dealership:list'))
    else:
        return render(request, 'dealership/add.html')
    
def delete(request):
    if request.POST:
        # delete the card
        pk = request.POST['pk']
        try:
            models.Vehicle.objects.get(pk=pk).delete()
            return redirect(reverse('vehicles:list'))
        except:
            print('pk not found')
            return redirect(reverse('dealership:list'))
    else:
        return render(request, 'dealership/delete.html')