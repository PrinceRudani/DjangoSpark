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
    path('admin_update_subcategory/<int:subcategory_id>/',
         views.admin_update_subcategory, name='admin_update_subcategory'),
]
