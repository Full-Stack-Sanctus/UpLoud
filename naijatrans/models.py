from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class UserLogin(AbstractUser):  # Inherit from AbstractUser
    email = models.EmailField(unique=True)  # Ensure email is unique
    password = models.CharField(max_length=128)
    
    class Meta:
        db_table = 'naijatrans_userlogin'  # Specify your custom table name
        

class Vehicle(models.Model):
    vehicle_number = models.CharField(max_length=10)
    capacity = models.IntegerField()
    route = models.CharField(max_length=100)
    current_speed = models.FloatField()  # To track overspeeding

class Ticket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    date_of_journey = models.DateField()
    seat_number = models.IntegerField()
    purchased_at = models.DateTimeField(auto_now_add=True)
