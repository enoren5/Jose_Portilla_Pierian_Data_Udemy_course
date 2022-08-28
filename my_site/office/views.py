from django.shortcuts import render
from . import models

# Create your views here.


def list_patients(request):
    #Collect all Patient instances and store them in a list:
    all_patients = models.Patient.objects.all()
    
    # Instantiate a single entry indicated by primary key 4
    c = models.Patient.objects.get(pk=4)
    # pull first name:
    c_name = c.first_name
    
    # Filtering entries based on date of birth <= 1950
    dob_filtered = models.Patient.objects.filter(dob__year__lte=1950)
    
    # final context declaration:
    context = {'patients':all_patients, 'full_adam':c,'adam':c_name, 'dob_filtered':dob_filtered}

    return render(request,'office/list.html',context=context)