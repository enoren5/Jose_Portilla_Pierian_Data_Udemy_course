from django.db import models

# Create your models here.

class Vehicle(models.Model):
    # pk
    brand = models.CharField(max_length=30)
    year = models.IntegerField()

    def __str__(self):
        return f"Vehicle is a {self.year} {self.brand}"