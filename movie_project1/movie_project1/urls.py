
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('credentials/',include('credentials.urls')),
    path('',include('mainapp.urls')),
    
    
]
