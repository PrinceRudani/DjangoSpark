from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('', include('category.urls')),
    path('', include('subcategory.urls')),
    path('', include('product.urls')),
]
