from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_view, name='search'),
    # Add other URL patterns as needed
]
