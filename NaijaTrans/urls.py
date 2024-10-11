from django.contrib import admin
from django.urls import path, include  # Include allows linking to app-level urls.py


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('naijatrans.urls')),  # Include the app-level URLs for userlogin app
    #path('api/', include('userregister.urls')),  # Include the app-level URLs for userregister app
]

