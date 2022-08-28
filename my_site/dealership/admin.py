from django.contrib import admin
from dealership.models import Vehicle


# Register your models here.

class VehicleAdmin(admin.ModelAdmin):
    # fields = ['year','brand']
    fieldsets = [
        ('TIME INFORMATION', {'fields':['year']}),
        ('VEHICLE INFORMATION', {'fields':['brand']}),
    ]
admin.site.register(Vehicle,VehicleAdmin)