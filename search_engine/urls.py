# In search_engine/urls.py

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('search.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


