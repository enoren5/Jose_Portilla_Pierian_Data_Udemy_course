from django.shortcuts import render, redirect
from django.urls import reverse
from . import models
from .forms import ReviewForm

def rental_review(request):
    
    # POST REQUEST -- > CONTENTS --> THANKYOU
    if request.method == "POST":
        form = ReviewForm(request.POST)
        
        # VALIDATE ROUTINE::
        if form.is_valid():
            print(form.cleaned_data)
            return redirect(reverse('car_rentals:thank_you'))
    # ELSE, Re-RENDER FORM
    else:
        form = ReviewForm
    return render(request, 'car_rentals/rental_review.html', context = {'form':form})

def thank_you(request):
    return render(request, 'car_rentals/thank_you.html')
