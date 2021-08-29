from django.contrib import admin
from django.urls import path, include
from ratPad import settings
from django.conf.urls.static import static

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),    
    path('accounts/', include('django.contrib.auth.urls')),        
    path('', include('pages.urls')),
    path('admin/', admin.site.urls), 
]
