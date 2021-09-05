from django.contrib import admin
from django.urls import path, include, reverse
from ratPad import settings
from django.conf.urls.static import static
from reports.views import ComputadorViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'computador', ComputadorViewset)

urlpatterns = [        
    path('reports/', include('reports.urls')),        
    path('grappelli/', include('grappelli.urls')),    
    path('accounts/', include('accounts.urls')),        
    path('', include('pages.urls')),
    path('admin/', admin.site.urls), 
    path('api/', include(router.urls)),    
]
if settings.DEBUG:    
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)