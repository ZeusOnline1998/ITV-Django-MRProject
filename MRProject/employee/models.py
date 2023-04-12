from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User


#Make email unique
User._meta.get_field('email')._unique = True

# Create your models here.

class Employee(models.Model):

    employee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    date_of_joining = models.DateField(default=timezone.now)
    status = models.CharField(max_length=10)


class Product(models.Model):

    def __str__(self):
        return self.name
    
    def save(self):

        self.name = self.name.title()
        self.company = self.company.title()
        super().save()
    
    name = models.CharField(max_length=256, null = False)
    company = models.CharField(max_length=256, null = False)
    image = models.ImageField(null = True, blank = True, upload_to= 'images/')
    price = models.IntegerField(null = False)
    employee = models.CharField(max_length=256)


class Doctor(models.Model):

    def __str__(self):
        return self.name

    def save(self):
        if not self.name.startswith('Dr.') or not self.name.startswith('dr.'):
            self.name = 'Dr. '+self.name
        self.name = self.name.title()
        self.specialisation = self.specialisation.title()
        self.location = self.location.title()

        super().save()
        
    name = models.CharField(max_length=256, null = False)
    specialisation = models.CharField(max_length=100, null = False)
    contact_number = models.CharField(max_length=10, null = False)
    location = models.CharField(max_length = 512 ,null = False)
    employee = models.CharField(max_length=256)


class DoctorSchedule(models.Model):

    def __str__(self):
        return f'Schedule for {self.doctor_name} on {self.date_of_schedule} {self.time_of_schedule}'

    doctor_name = models.CharField(max_length=256)
    date_of_schedule = models.DateField(null = False, blank = False)
    time_of_schedule = models.TimeField(null = False, blank = False)
    employee = models.CharField(max_length=256)


class DealsDetail(models.Model):

    def __str__(self):
        return f'Doctor - {self.doctor_name} : Product - {self.product_name}'

    doctor_name = models.CharField(max_length=256)
    product_name = models.CharField(max_length=256)
    quantity_ordered = models.IntegerField()
    employee = models.CharField(max_length=256)


    