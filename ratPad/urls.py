from django.urls import path, include, reverse
from django.contrib import admin
from django.conf.urls.static import static

from rest_framework import routers
import debug_toolbar

from reports.views import ComputadorViewset
from ratPad import settings


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
    urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]