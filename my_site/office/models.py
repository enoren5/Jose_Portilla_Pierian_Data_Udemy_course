from django.db import models
from datetime import datetime

# Create your models here.
class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    dob = models.DateField() # Proper more precicse date of birth to be calculated in method below
    
    def calculated_age(self):
        return self.dob - datetime.date(now) 

    def __str__(self):
        return f"{self.first_name} {self.last_name} is {self.age} years old"

    def __repr__(self):
        return f"{self.first_name} {self.last_name} is {self.age} years old"