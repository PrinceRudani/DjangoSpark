from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path('admin_load_product/', views.admin_load_product,
         name='admin_load_product'),
    path('admin_load_ajax/', views.admin_load_ajax, name='admin_load_ajax'),
    path('admin_insert_product/', views.admin_insert_product,
         name='admin_insert_product'),
    path('admin_view_product/', views.admin_view_product,
         name='admin_view_product'),
    path('admin_delete_product/', views.admin_delete_product,
         name='admin_delete_product'),
    path('admin_edit_product/<int:product_id>/', views.admin_edit_product,
         name='admin_edit_product'),
    path('admin_update_product/<int:product_id>/', views.admin_update_product,
         name='admin_update_product'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
