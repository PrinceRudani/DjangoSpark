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
from django.urls import path

from category import views

urlpatterns = [
    path('admin_load_category/', views.admin_load_category,
         name='admin_load_category'),
    path('admin_insert_category', views.admin_insert_category,
         name='admin_insert_category'),
    path('admin_view_category/', views.admin_view_category,
         name='admin_view_category'),
    path('admin_delete_category/', views.admin_delete_category,
         name='admin_delete_category'),
    path('admin_edit_category/', views.admin_edit_category,
         name='admin_edit_category'),
    path("admin_update_category/", views.admin_update_category,
         name="admin_update_category"),
]
