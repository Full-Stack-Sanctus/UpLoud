from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings

# Custom User Manager
class UserLoginManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves a regular user with the given email and password.
        """
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Creates and saves a superuser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

# Custom User Model
class UserLogin(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)  # Ensure email is unique
    password = models.CharField(max_length=128)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserLoginManager()  # Use the custom manager

    USERNAME_FIELD = 'email'  # Use email as the username field
    REQUIRED_FIELDS = []  # Add any additional required fields
    
    class Meta:
        db_table = 'naijatrans_userlogin'  # Specify your custom table name

# Vehicle Model
class Vehicle(models.Model):
    vehicle_number = models.CharField(max_length=10)
    capacity = models.IntegerField()
    route = models.CharField(max_length=100)
    current_speed = models.FloatField()  # To track overspeeding

# Ticket Model
class Ticket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    date_of_journey = models.DateField()
    seat_number = models.IntegerField()
    purchased_at = models.DateTimeField(auto_now_add=True)  # Fix the typo here
