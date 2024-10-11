from django.contrib import admin
from django.urls import path, include  # Include allows linking to app-level urls.py

from naijatrans.models import UserLogin  # or your custom user model name

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('UserLogin.urls')),  # Include the app-level URLs for userlogin app
    #path('api/', include('userregister.urls')),  # Include the app-level URLs for userregister app
]

