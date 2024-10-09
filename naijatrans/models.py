from django.db import models

class UserLogin(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=15)

class Vehicle(models.Model):
    vehicle_number = models.CharField(max_length=10)
    capacity = models.IntegerField()
    route = models.CharField(max_length=100)
    current_speed = models.FloatField()  # To track overspeeding

class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    date_of_journey = models.DateField()
    seat_number = models.IntegerField()
    purchased_at = models.DateTimeField(auto_now_add=True)
