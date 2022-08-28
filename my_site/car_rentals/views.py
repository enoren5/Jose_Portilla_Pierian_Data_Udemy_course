from django.shortcuts import render, redirect
from django.urls import reverse
from . import models

def rental_review(request):
    return render(request, 'car_rentals/rental_review.html')

def thank_you(request):
    return render(request, 'car_rentals/thank_you.html')
