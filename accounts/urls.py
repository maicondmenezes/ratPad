from django.urls import path, include
from django.contrib.auth.views import LoginView
app_name = 'accounts'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),    
]
