# DjangoProject/urls.py (main project's urls.py)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin URLs
    path('', include('base.urls')),  # Include base app URLs
    path('', include('category.urls')),  # Include category app URLs
    path('', include('subcategory.urls'))
    # Include subcategory app URLs
]
