from django.db import models
# from datetime import date
from datetime import datetime, date
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
import humanize

# Create your models here.

class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(120)])
    heartrate = models.IntegerField(default=60,validators=[MinValueValidator(50), MaxValueValidator(180)])
    dob = models.DateTimeField(default=datetime(1957,6,6)) # Proper more precise date of birth to be calculated in method below
    
    def calculated_age(self):
        td = timezone.now() - self.dob
        return str(td)
        # return humanize.naturaldate(str(td))
        #return td.strftime("%Y %m %d")


    def __str__(self):
        return f"{self.first_name} {self.last_name} is {self.age} years old"

    def __repr__(self):
        return f"{self.first_name} {self.last_name} is {self.age} years old"