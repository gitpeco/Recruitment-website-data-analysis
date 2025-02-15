from django.contrib import admin
from django.urls import path, include
from Crawl.views import listorders

urlpatterns = [
    path('admin/', admin.site.urls),

    path('Crawl/', include('Crawl.urls')),

    path('api/mgr/',include('mgr.urls')),
]
