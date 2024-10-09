from django.urls import path
from .views import register, login, profile

urlpatterns = [
    
    path('api/auth/check/', check_authentication_anonymous, name='check-authentication'),
   

    path('api/register/', register),
    path('api/login/', login),
    path('api/profile/', profile),
]
