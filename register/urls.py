from django.urls import path

from . import views

urlpatterns = [
    path("admin_load_register/", views.admin_load_register, name="admin_load_register"),
    path(
        "admin_insert_register/",
        views.admin_insert_register,
        name="admin_insert_register",
    ),
]
