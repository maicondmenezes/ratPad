from django.urls import path
from .views import HomePageView, AboutPageView

app_name = 'pages'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('sobre/', AboutPageView.as_view(), name='about'),    
]