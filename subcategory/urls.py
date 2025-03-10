"""
URL configuration for DjangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# subcategory/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('admin_load_subcategory/', views.admin_load_subcategory,
         name='admin_load_subcategory'),
    path('admin_insert_subcategory/', views.admin_insert_subcategory,
         name='admin_insert_subcategory'),
    path('admin_view_subcategory/', views.admin_view_subcategory,
         name='admin_view_subcategory'),
    path('admin_delete_subcategory/', views.admin_delete_subcategory,
         name='admin_delete_subcategory'),
    path('admin_edit_subcategory/', views.admin_edit_subcategory,
             name='admin_edit_subcategory'),
    path('admin_update_subcategory/', views.admin_update_subcategory,
             name='admin_update_subcategory'),
]
