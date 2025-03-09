from django.contrib import admin
from django.urls import path, include  # Import include

urlpatterns = [
    path('', include('base.urls')),
    path('', include('category.urls')),
    # path('', include('subcategory.urls')),

    path('admin/', admin.site.urls),
]
